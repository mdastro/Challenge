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

    # Loading the datasets ---------------------------------------------------------------------------------------------
    my_data_z021        = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/total_file_z021.csv', delimiter=',',
                                     dtype=str)[1:,:]
    my_data_z050        = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/total_file_z050.csv', delimiter=',',
                                     dtype=str)[1:,:]
    my_data_z090        = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/total_file_z090.csv', delimiter=',',
                                     dtype=str)
    jpas_filters_header = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/header.txt', dtype=str)
    jpas_filters_header = jpas_filters_header[:,1].T
    my_data_sdss        = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/table_sdss_galaxies.txt', dtype=str)
    sdss_redshifts      = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/redshifts.txt', dtype=str)[:,1]
    sdss_filters_header = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/jpas_filters_header.txt', dtype=str)

    # dictionary_z021 = {}
    # for i in range(len(my_data_z021[0, :])):                                   # Converting numpy array into dictionary
    #     dictionary_z021[my_data_z021[0, i]] = np.array(my_data_z021[0 + 1:, i], dtype=str)

    # Separating what is photometry and the errors -- first line is the photometric data and the second is the error of
    # such data --------------------------------------------------------------------------------------------------------
    filter_info_z021  = my_data_z021[0::2]
    filter_error_z021 = my_data_z021[1::2]

    filter_info_z050  = my_data_z050[0::2]
    filter_error_z050 = my_data_z050[1::2]

    filter_info_z090  = my_data_z090[0::2]
    filter_error_z090 = my_data_z090[1::2]

    filter_info_sdss  = my_data_sdss[0::2]
    filter_error_sdss = my_data_sdss[1::2]

    # Creating a new header --------------------------------------------------------------------------------------------
    new_header = ['galaxy_id']
    for header in range(jpas_filters_header.size):
        new_header.append(jpas_filters_header[header])
        new_header.append('error_'+jpas_filters_header[header])
    new_header.append('redshift')                                                  # Appending objects' redshift.
    new_header = np.array(new_header)

    new_sdss_header = ['galaxy_id']
    for header in range(sdss_filters_header.size):
        new_sdss_header.append(sdss_filters_header[header])
        new_sdss_header.append('error_'+sdss_filters_header[header])
    new_sdss_header.append('redshift')                                            # Appending objects' redshift.
    new_sdss_header = np.array(new_sdss_header)

    # Creating a new array with the info in the following order: "galaxy_id, photometry1, photo1_error, ..., redshift" -
    galaxies_z021 = []
    for i in range(filter_info_z021[:, 0].size):
        galaxies_z021.append(i+1)                   # appending the galaxy identifier (number)
        for j in range(filter_info_z021[0, :].size):
            galaxies_z021.append(filter_info_z021[i][j])
            galaxies_z021.append(filter_error_z021[i][j])
        galaxies_z021.append(0.021)
    galaxies_z021 = np.array(galaxies_z021)
    galaxies_z021 = np.reshape(galaxies_z021, (filter_info_z021[:, 0].size, filter_info_z021[0, :].size * 2 + 2))

    galaxies_z050 = []
    for i in range(filter_info_z050[:, 0].size):
        galaxies_z050.append(i+1)                   # appending the galaxy identifier (number)
        for j in range(filter_info_z050[0, :].size):
            galaxies_z050.append(filter_info_z050[i][j])
            galaxies_z050.append(filter_error_z050[i][j])
        galaxies_z050.append(0.050)
    galaxies_z050 = np.array(galaxies_z050)
    galaxies_z050 = np.reshape(galaxies_z050, (filter_info_z050[:, 0].size, filter_info_z050[0, :].size * 2 + 2))

    galaxies_z090 = []
    for i in range(filter_info_z090[:, 0].size):
        galaxies_z090.append(i+1)                   # appending the galaxy identifier (number)
        for j in range(filter_info_z090[0, :].size):
            galaxies_z090.append(filter_info_z090[i][j])
            galaxies_z090.append(filter_error_z090[i][j])
        galaxies_z090.append(0.090)
    galaxies_z090 = np.array(galaxies_z090)
    galaxies_z090 = np.reshape(galaxies_z090, (filter_info_z090[:, 0].size, filter_info_z090[0, :].size * 2 + 2))

    galaxies_sdss = []
    for i in range(filter_info_sdss[:, 0].size):
        galaxies_sdss.append(i+1)                   # appending the galaxy identifier (number)
        for j in range(filter_info_sdss[0, :].size):
            galaxies_sdss.append(filter_info_sdss[i][j])
            galaxies_sdss.append(filter_error_sdss[i][j])
        galaxies_sdss.append(sdss_redshifts[i])
    galaxies_sdss = np.array(galaxies_sdss)
    galaxies_sdss = np.reshape(galaxies_sdss, (filter_info_sdss[:, 0].size, filter_info_sdss[0, :].size * 2 + 2))


    # Stacking the new header on the top of the dataset ----------------------------------------------------------------
    new_galaxies_z021 = np.vstack((new_header, galaxies_z021))
    new_galaxies_z050 = np.vstack((new_header, galaxies_z050))
    new_galaxies_z090 = np.vstack((new_header, galaxies_z090))
    new_galaxies_sdss = np.vstack((new_sdss_header, galaxies_sdss))

    # Saving the results using pandas ----------------------------------------------------------------------------------
    new_galaxies_z021 = pd.DataFrame(new_galaxies_z021)
    new_galaxies_z021.to_csv('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/photocat_challenge_z021.csv', sep=',',
                             header=None, index=False)

    new_galaxies_z050 = pd.DataFrame(new_galaxies_z050)
    new_galaxies_z050.to_csv('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/photocat_challenge_z050.csv', sep=',',
                             header=None, index=False)

    new_galaxies_z090 = pd.DataFrame(new_galaxies_z090)
    new_galaxies_z090.to_csv('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/photocat_challenge_z090.csv', sep=',',
                             header=None, index=False)

    new_galaxies_sdss = pd.DataFrame(new_galaxies_sdss)
    new_galaxies_sdss.to_csv('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/photocat_challenge_sdss.csv', sep=',',
                             header=None, index=False)
