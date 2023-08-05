import json
import random
from dataclasses import dataclass
from datetime import datetime
from typing import List
from typing import Tuple

import numpy as np
import pytest
from astropy.io import fits
from astropy.time import Time
from astropy.time import TimeDelta
from dkist_header_validator import spec122_validator
from dkist_processing_common._util.scratch import WorkflowFileSystem
from dkist_processing_common.models.tags import Tag

from dkist_processing_visp.models.tags import VispTag
from dkist_processing_visp.parsers.visp_l0_fits_access import VispL0FitsAccess
from dkist_processing_visp.tasks.science import ScienceCalibration
from dkist_processing_visp.tests.conftest import FakeGQLClient
from dkist_processing_visp.tests.conftest import generate_fits_frame
from dkist_processing_visp.tests.conftest import VispConstantsDb
from dkist_processing_visp.tests.conftest import VispHeadersValidObserveFrames
from dkist_processing_visp.tests.conftest import VispTestingParameters


@dataclass
class VispScienceTestingParameters(VispTestingParameters):
    visp_beam_border: int = 10


@pytest.fixture(scope="function", params=["Full Stokes", "Stokes-I"])
def science_calibration_task(
    tmp_path, recipe_run_id, assign_input_dataset_doc_to_task, init_visp_constants_db, request
):
    num_dsps_repeats = 2
    num_beams = 2
    num_raster_steps = 2
    exposure_time = 0.02  # From VispHeadersValidObserveFrames fixture
    if request.param == "Full Stokes":
        num_modstates = 2
        polarimeter_mode = "observe_polarimetric"
    else:
        num_modstates = 1
        polarimeter_mode = "observe_intensity"
    array_shape = (1, 20, 10)
    intermediate_shape = (10, 10)
    dataset_shape = (
        num_beams * num_dsps_repeats * num_raster_steps * num_modstates,
    ) + array_shape[1:]

    constants_db = VispConstantsDb(
        POLARIMETER_MODE=polarimeter_mode,
        NUM_MODSTATES=num_modstates,
        NUM_DSPS_REPEATS=num_dsps_repeats,
        NUM_RASTER_STEPS=num_raster_steps,
        NUM_BEAMS=num_beams,
        OBSERVE_EXPOSURE_TIMES=(exposure_time,),
    )
    init_visp_constants_db(recipe_run_id, constants_db)
    with ScienceCalibration(
        recipe_run_id=recipe_run_id, workflow_name="science_calibration", workflow_version="VX.Y"
    ) as task:
        try:  # This try... block is here to make sure the dbs get cleaned up if there's a failure in the fixture
            all_zeros = np.zeros(intermediate_shape)
            all_ones = np.ones(intermediate_shape)
            task.scratch = WorkflowFileSystem(
                scratch_base_path=tmp_path, recipe_run_id=recipe_run_id
            )
            assign_input_dataset_doc_to_task(task, VispScienceTestingParameters())
            # Create fake demodulation matrices
            demod_matrices = np.zeros((1, 1, 4, num_modstates))
            for modstate in range(num_modstates):
                demod_matrices[0, 0, :, modstate] = [1, 2, 3, 4]
            for beam in range(num_beams):
                demod_hdul = fits.HDUList([fits.PrimaryHDU(data=demod_matrices)])
                task.fits_data_write(
                    hdu_list=demod_hdul,
                    tags=[
                        VispTag.intermediate(),
                        VispTag.task("DEMOD_MATRICES"),
                        VispTag.beam(beam + 1),
                    ],
                )

            # Create fake geometric objects
            angle = np.array([0.0])
            offset = np.array([0.0, 0.0])
            spec_shift = np.zeros(intermediate_shape[0])
            for beam in range(1, num_beams + 1):
                task.intermediate_frame_helpers_write_arrays(
                    arrays=angle, beam=beam, task="GEOMETRIC_ANGLE"
                )
                task.intermediate_frame_helpers_write_arrays(
                    arrays=spec_shift, beam=beam, task="GEOMETRIC_SPEC_SHIFTS"
                )
                for modstate in range(1, num_modstates + 1):
                    task.intermediate_frame_helpers_write_arrays(
                        arrays=offset, beam=beam, modstate=modstate, task="GEOMETRIC_OFFSET"
                    )

            # Create fake dark intermediate arrays
            for beam in range(1, num_beams + 1):
                task.intermediate_frame_helpers_write_arrays(
                    all_zeros, beam=beam, task="DARK", exposure_time=exposure_time
                )

            # Create fake solar_gain intermediate arrays
            for beam in range(1, num_beams + 1):
                for modstate in range(1, num_modstates + 1):
                    gain_hdul = fits.HDUList([fits.PrimaryHDU(data=all_ones)])
                    task.fits_data_write(
                        hdu_list=gain_hdul,
                        tags=[
                            VispTag.intermediate(),
                            VispTag.frame(),
                            VispTag.task("SOLAR_GAIN"),
                            VispTag.beam(beam),
                            VispTag.modstate(modstate),
                        ],
                    )

            # Create fake observe arrays
            start_time = datetime.now()
            for dsps_repeat in range(1, num_dsps_repeats + 1):
                for raster_step in range(0, num_raster_steps):
                    for modstate in range(1, num_modstates + 1):
                        ds = VispHeadersValidObserveFrames(
                            dataset_shape=dataset_shape,
                            array_shape=array_shape,
                            time_delta=10,
                            num_dsps_repeats=num_dsps_repeats,
                            dsps_repeat=dsps_repeat,
                            num_raster_steps=num_raster_steps,
                            raster_step=raster_step,
                            num_modstates=num_modstates,
                            modstate=modstate,
                            start_time=start_time,
                        )
                        header_generator = (
                            spec122_validator.validate_and_translate_to_214_l0(
                                d.header(), return_type=fits.HDUList
                            )[0].header
                            for d in ds
                        )

                        hdul = generate_fits_frame(
                            header_generator=header_generator, shape=array_shape
                        )
                        task.fits_data_write(
                            hdu_list=hdul,
                            tags=[
                                VispTag.task("OBSERVE"),
                                VispTag.raster_step(raster_step),
                                VispTag.dsps_repeat(dsps_repeat),
                                VispTag.modstate(modstate),
                                VispTag.input(),
                                VispTag.frame(),
                                VispTag.exposure_time(exposure_time),
                            ],
                        )

            yield task, request.param
        except:
            raise
        finally:
            task.scratch.purge()
            task.constants._purge()


@pytest.fixture(scope="session")
def headers_with_dates() -> Tuple[List[fits.Header], str, int, int]:
    num_headers = 5
    start_time = "1969-12-06T18:00:00"
    exp_time = 12
    time_delta = 10
    ds = VispHeadersValidObserveFrames(
        dataset_shape=(num_headers, 4, 4),
        array_shape=(1, 4, 4),
        time_delta=time_delta,
        num_dsps_repeats=1,
        dsps_repeat=1,
        num_raster_steps=1,
        raster_step=1,
        num_modstates=num_headers,
        modstate=1,
        start_time=datetime.fromisoformat(start_time),
    )
    headers = [
        spec122_validator.validate_and_translate_to_214_l0(d.header(), return_type=fits.HDUList)[
            0
        ].header
        for d in ds
    ]
    random.shuffle(headers)  # Shuffle to make sure they're not already in time order
    for h in headers:
        h["TEXPOSUR"] = exp_time  # Exposure time, in ms

    return headers, start_time, exp_time, time_delta


def test_science_calibration_task(science_calibration_task, mocker):
    """
    Given: A ScienceCalibration task
    When: Calling the task instance
    Then: There are the expected number of science frames with the correct tags applied
    """

    mocker.patch(
        "dkist_processing_common.tasks.mixin.metadata_store.GraphQLClient", new=FakeGQLClient
    )

    # When
    task, polarization_mode = science_calibration_task
    task()

    # Then
    tags = [
        VispTag.calibrated(),
        VispTag.frame(),
    ]
    files = list(task.read(tags=tags))
    if polarization_mode == "Full Stokes":
        # 2 raster steps * 2 dsps repeats * 4 stokes params = 16 frames
        assert len(files) == 16
    elif polarization_mode == "Stokes-I":
        # 2 raster steps * 2 dsps repeats * 1 stokes param = 4 frames
        assert len(files) == 4
    for file in files:
        hdul = fits.open(file)
        assert hdul[0].data.shape == (1, 10, 10)  # 1 from re-dummification
        assert "DATE-BEG" in hdul[0].header.keys()
        assert "DATE-END" in hdul[0].header.keys()

    quality_files = task.read(tags=[Tag.quality("TASK_TYPES")])
    for file in quality_files:
        with file.open() as f:
            data = json.load(f)
            assert isinstance(data, dict)
            assert data["total_frames"] == task.scratch.count_all(
                tags=[VispTag.input(), VispTag.frame(), VispTag.task("OBSERVE")]
            )

    # Test that all beam 1 intermediate arrays have matching beam 2 arrays
    tags = [VispTag.beam(1), VispTag.intermediate(), VispTag.task("INTERMEDIATE_ARRAYS")]
    beam1_fits_access = task.fits_data_read_fits_access(
        tags=tags,
        cls=VispL0FitsAccess,
    )
    # This will raise a runtime error if a matching file does not exist
    for beam1_obj in beam1_fits_access:
        task.matching_beam_2_fits_access(beam1_obj)


def test_compute_date_keys(headers_with_dates, recipe_run_id, init_visp_constants_db):
    """
    Given: A set of headers with different DATE-OBS values
    When: Computing the time over which the headers were taken
    Then: A header with correct DATE-BEG, DATE-END, and DATE-AVG keys is returned
    """
    headers, start_time, exp_time, time_delta = headers_with_dates
    constants_db = VispConstantsDb()
    init_visp_constants_db(recipe_run_id, constants_db)
    with ScienceCalibration(
        recipe_run_id=recipe_run_id, workflow_name="science_calibration", workflow_version="VX.Y"
    ) as task:
        final_header = task._compute_date_keys(headers)

    date_end = (
        Time(start_time)
        + (len(headers) - 1) * TimeDelta(time_delta, format="sec")
        + TimeDelta(exp_time / 1000.0, format="sec")
    ).isot

    assert final_header["DATE-BEG"] == start_time
    assert final_header["DATE-END"] == date_end
