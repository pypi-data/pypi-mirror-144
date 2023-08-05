
#  Module for 2d saturation
#
import logging
import numpy as np

from ..datamodels import dqflags
from ..lib import reffile_utils
from . import x_irs2

from stcal.saturation.saturation import flag_saturated_pixels

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

DONOTUSE = dqflags.pixel['DO_NOT_USE']
SATURATED = dqflags.pixel['SATURATED']
AD_FLOOR = dqflags.pixel['AD_FLOOR']
NO_SAT_CHECK = dqflags.pixel['NO_SAT_CHECK']
ATOD_LIMIT = 65535.  # Hard DN limit of 16-bit A-to-D converter


def flag_saturation(input_model, ref_model):
    """
    Short Summary
    -------------
    Call function in stcal for flagging for saturated pixels.

    Parameters
    ----------
    input_model : `~jwst.datamodels.RampModel`
        The input science data to be corrected

    ref_model : `~jwst.datamodels.SaturationModel`
        Saturation reference file data model

    Returns
    -------
    output_model : `~jwst.datamodels.RampModel`
        Data model with saturation, A/D floor, and do not use flags set in
        the GROUPDQ array
    """

    data = input_model.data

    # Create the output model as a copy of the input
    output_model = input_model.copy()
    gdq = output_model.groupdq
    pdq = output_model.pixeldq

    # Extract subarray from saturation reference file, if necessary
    if reffile_utils.ref_matches_sci(input_model, ref_model):
        sat_thresh = ref_model.data
        sat_dq = ref_model.dq
    else:
        log.info('Extracting reference file subarray to match science data')
        ref_sub_model = reffile_utils.get_subarray_model(input_model, ref_model)
        sat_thresh = ref_sub_model.data.copy()
        sat_dq = ref_sub_model.dq.copy()
        ref_sub_model.close()

    gdq_new, pdq_new = flag_saturated_pixels(data, gdq, pdq, sat_thresh,
                                             sat_dq, ATOD_LIMIT, dqflags.pixel)

    # Save the flags in the output GROUPDQ array
    output_model.groupdq = gdq_new

    # Save the NO_SAT_CHECK flags in the output PIXELDQ array
    output_model.pixeldq = pdq_new

    return output_model


def irs2_flag_saturation(input_model, ref_model):
    """
    Short Summary
    -------------
    For NIRSPEC IRS2 mode only, apply flagging for saturation based on threshold
    values stored in the saturation reference file and A/D floor based on
    testing for 0 DN values. For A/D floor flagged groups, the DO_NOT_USE flag
    is also set.

    Parameters
    ----------
    input_model : `~jwst.datamodels.RampModel`
        The input science data to be corrected

    ref_model : `~jwst.datamodels.SaturationModel`
        Saturation reference file data model

    Returns
    -------
    output_model : `~jwst.datamodels.RampModel`
        Data model with saturation, A/D floor, and do not use flags set in
        the GROUPDQ array
    """

    data = input_model.data
    nints = data.shape[0]
    ngroups = data.shape[1]
    detector = input_model.meta.instrument.detector

    # create a mask of the appropriate size
    irs2_mask = x_irs2.make_mask(input_model)

    # Create the output model as a copy of the input
    output_model = input_model.copy()
    groupdq = output_model.groupdq

    # Extract subarray from saturation reference file, if necessary
    if reffile_utils.ref_matches_sci(input_model, ref_model):
        sat_thresh = ref_model.data
        sat_dq = ref_model.dq
    else:
        log.info('Extracting reference file subarray to match science data')
        ref_sub_model = reffile_utils.get_subarray_model(input_model, ref_model)
        sat_thresh = ref_sub_model.data.copy()
        sat_dq = ref_sub_model.dq.copy()
        ref_sub_model.close()

    # For pixels flagged in reference file as NO_SAT_CHECK,
    # set the saturation check threshold to the A-to-D converter limit.
    sat_thresh[np.bitwise_and(sat_dq, NO_SAT_CHECK) == NO_SAT_CHECK] = ATOD_LIMIT

    # Also reset NaN values in the saturation threshold array to the
    # A-to-D limit and flag them with NO_SAT_CHECK
    sat_dq[np.isnan(sat_thresh)] |= NO_SAT_CHECK
    sat_thresh[np.isnan(sat_thresh)] = ATOD_LIMIT

    flagarray = np.zeros(data.shape[-2:], dtype=groupdq.dtype)
    flaglowarray = np.zeros(data.shape[-2:], dtype=groupdq.dtype)
    for ints in range(nints):
        for group in range(ngroups):
            # Update the 4D groupdq array with the saturation flag.
            sci_temp = x_irs2.from_irs2(data[ints, group, :, :],
                                        irs2_mask, detector)
            # check for saturation
            flag_temp = np.where(sci_temp >= sat_thresh, SATURATED, 0)
            # check for A/D floor
            flaglow_temp = np.where(sci_temp <= 0, AD_FLOOR | DONOTUSE, 0)
            # Copy temps into flagarrays.
            x_irs2.to_irs2(flagarray, flag_temp, irs2_mask, detector)
            x_irs2.to_irs2(flaglowarray, flaglow_temp, irs2_mask, detector)

            # for saturation, the flag is set in the current plane
            # and all following planes.
            np.bitwise_or(groupdq[ints, group:, :, :], flagarray,
                          groupdq[ints, group:, :, :])
            # for A/D floor, the flag is only set of the current plane
            np.bitwise_or(groupdq[ints, group, :, :], flaglowarray,
                          groupdq[ints, group, :, :])

    # Save the flags in the output GROUPDQ array
    output_model.groupdq = groupdq

    n_sat = np.any(np.any(np.bitwise_and(groupdq, SATURATED), axis=0), axis=0).sum()
    log.info(f'Detected {n_sat} saturated pixels')
    n_floor = np.any(np.any(np.bitwise_and(groupdq, AD_FLOOR), axis=0), axis=0).sum()
    log.info(f'Detected {n_floor} A/D floor pixels')

    # Save the NO_SAT_CHECK flags in the output PIXELDQ array
    pixeldq_temp = x_irs2.from_irs2(output_model.pixeldq, irs2_mask,
                                    detector)
    pixeldq_temp = np.bitwise_or(pixeldq_temp, sat_dq)
    x_irs2.to_irs2(output_model.pixeldq, pixeldq_temp, irs2_mask, detector)

    return output_model
