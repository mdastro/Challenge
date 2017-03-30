#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    This program generates simulated J-PAS photometry to SDSS spectra.

    @author:  Maria Luiza L. Dantas
    @date:    2017.03.30
    @version: 0.0.1 - incomplete test version
"""

import numpy as np
import os
import pysynphot as s

# ======================================================================================================================
# Main thread

if __name__ == '__main__':

    # Loading the datasets ---------------------------------------------------------------------------------------------
    jpas_filters      = '/home/mldantas/Dropbox/DoutoradoIAG/Challenge/Filters/JPAS_filters'
    test_specs        = '/home/mldantas/Dropbox/DoutoradoIAG/Challenge/Sanity_Check/Specs'
    jpas_filters_list = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/Filters/jpas_filters_list.txt',
                                   dtype=str)

    # s.refs.PRIMARY_AREA = 4400                                                         # T80 M1 effective area in cm^2

    # jpas_filters = np.loadtxt(jpas_filters_path, dtype=str)
    for each_spectrum in os.listdir(test_specs):
        for jpas_filters in jpas_filters_list:
            filter_name = jpas_filters.split('.')[0]
            jpas_filter   = s.FileBandpass(jpas_filters)
            sdss_spectrum = s.FileSpectrum(test_specs)
            photometry = s.Observation(sdss_spectrum,jpas_filter,binset=np.arange(3000, 11000, 1))
            #TODO Check what this last command means
            # The "binset" establishes the sampling.

            #TODO finish and save the datasets

