#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    This program reads .csv files with the simulated galaxies and saves it in the correct format for BEAGLE to load and
    run,
    @author:  Maria Luiza L. Dantas
    @date:    2017.03.08
    @version: 0.0.1
"""

import numpy as np
import pandas as pd

# ======================================================================================================================
# Main thread

if __name__ == '__main__':

    my_data_z021        = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/total_file_z021.csv', delimiter=',',
                                     dtype=str)[1:,:]
    my_data_z050        = '/home/mldantas/Dropbox/DoutoradoIAG/Challenge/total_file_z050.csv'
    my_data_z090        = '/home/mldantas/Dropbox/DoutoradoIAG/Challenge/total_file_z090.csv'
    jpas_filters_header = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/jpas_filters_header.txt', dtype=str)
    jpas_filters_header = jpas_filters_header.T
    jpas_errors_header  = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/jpas_filterserrors_header.txt',
                                     dtype=str)
    jpas_errors_header = jpas_errors_header.T
    # my_data_sdss   = '/home/mldantas/Dropbox/DoutoradoIAG/Challenge/table_sdss_galaxies.dat'
    # sdss_redshifts = '/home/mldantas/Dropbox/DoutoradoIAG/Challenge/redshifts.dat'

    dictionary_z021 = {}
    for i in range(len(my_data_z021[0, :])):                                   # Converting numpy array into dictionary
        dictionary_z021[my_data_z021[0, i]] = np.array(my_data_z021[0 + 1:, i], dtype=str)

    filter_info  = my_data_z021[0::2]
    filter_error = my_data_z021[1::2]

    new_header = []
    for header in range(jpas_filters_header.size):
        new_header.append(jpas_errors_header[header])
        new_header.append(jpas_filters_header[header])
    new_header.append(jpas_errors_header[-1])
    new_header = np.array(new_header)

    galaxies_z021 = []
    # galaxies_z021.append(list(new_header))
    for i in range(filter_info[:,0].size):
        galaxies_z021.append(i+1)
        for j in range(filter_info[0,:].size):
            galaxies_z021.append(filter_info[i][j])
            galaxies_z021.append(filter_error[i][j])
    galaxies_z021 = np.array(galaxies_z021).reshape((filter_info[:, 0].size, filter_info[0, :].size * 2 + 1))


    np.savetxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/photocat_challenge_z021.csv', galaxies_z021,
               delimiter=',', newline='\n')