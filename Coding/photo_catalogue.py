#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    This program reads .csv files with the simulated galaxies and saves it in the correct format for BEAGLE to load and
    run,
    This version has many improvements in terms of generating the catalogs.
    @author:  Maria Luiza L. Dantas
    @date:    2017.05.29
    @version: 0.0.3
"""

import numpy as np
import pandas as pd
import pyfits
import os


# Main thread

if __name__ == '__main__':

    # Loading the datasets ---------------------------------------------------------------------------------------------
    my_data_z021        = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/PhotoCats/total_file_z021_fnu.csv',
                                     delimiter=',', dtype=str)
    my_data_z050        = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/PhotoCats/total_file_z050_fnu.csv',
                                     delimiter=',', dtype=str)
    my_data_z090        = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/PhotoCats/total_file_z090_fnu.csv',
                                     delimiter=',', dtype=str)
    jpas_filters_header = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/header.txt', dtype=str)
    jpas_filters_header = jpas_filters_header[:, 1].T
    my_data_sdss        = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/PhotoCats/'
                                     'table_sdss_galaxies_fnu.csv', delimiter=',', dtype=str)
    sdss_redshifts      = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/redshifts.txt', dtype=str)[:,1]
    sdss_filters_header = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/jpas_filters_header.txt', dtype=str)

    results_path = '/home/mldantas/Dropbox/DoutoradoIAG/Challenge/PhotoCats/fnu'


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
        galaxies_z021.append(0.21)
    galaxies_z021 = np.array(galaxies_z021)
    galaxies_z021 = np.reshape(galaxies_z021, (filter_info_z021[:, 0].size, filter_info_z021[0, :].size * 2 + 2))

    galaxies_z050 = []
    for i in range(filter_info_z050[:, 0].size):
        galaxies_z050.append(i+1)                   # appending the galaxy identifier (number)
        for j in range(filter_info_z050[0, :].size):
            galaxies_z050.append(filter_info_z050[i][j])
            galaxies_z050.append(filter_error_z050[i][j])
        galaxies_z050.append(0.50)
    galaxies_z050 = np.array(galaxies_z050)
    galaxies_z050 = np.reshape(galaxies_z050, (filter_info_z050[:, 0].size, filter_info_z050[0, :].size * 2 + 2))

    galaxies_z090 = []
    for i in range(filter_info_z090[:, 0].size):
        galaxies_z090.append(i+1)                   # appending the galaxy identifier (number)
        for j in range(filter_info_z090[0, :].size):
            galaxies_z090.append(filter_info_z090[i][j])
            galaxies_z090.append(filter_error_z090[i][j])
        galaxies_z090.append(0.90)
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


    # Stacking the datasets --------------------------------------------------------------------------------------------
    galaxies_all_reshifts = np.vstack((new_header, galaxies_z021, galaxies_z050, galaxies_z090))
    galaxies_sdss_new     = np.vstack((new_sdss_header, galaxies_sdss))

    # Separating among JPAS and JPLUS surveys --------------------------------------------------------------------------
    ## JPAS ------------------------------------------------------------------------------------------------------------
    cat_jpas_all = np.hstack((galaxies_all_reshifts[:, :111], galaxies_all_reshifts[:, 141:143],
                              galaxies_all_reshifts[:, 115:117], galaxies_all_reshifts[:, 111:115],
                              galaxies_all_reshifts[:, 143:]))
    cat_jpas_sdss = np.hstack((galaxies_sdss_new[:, :111], galaxies_sdss_new[:, 115:117], galaxies_sdss_new[:, 111:115],
                               galaxies_sdss_new[:, 132:]))

    ## JPLUS -----------------------------------------------------------------------------------------------------------

    cat_jplus_all = np.hstack((galaxies_all_reshifts[:,0:1], galaxies_all_reshifts[:,117:131],
                                galaxies_all_reshifts[:,137:139], galaxies_all_reshifts[:,131:133],
                                galaxies_all_reshifts[:,135:137], galaxies_all_reshifts[:,133:135],
                               galaxies_all_reshifts[:,139:141], galaxies_all_reshifts[:,143:]))

    cat_jplus_sdss = np.hstack((galaxies_sdss_new[:,0:1], galaxies_sdss_new[:,117:]))

    # Tranforming into data frames and saving into csv and fits files --------------------------------------------------
    ## fits version ----------------------------------------------------------------------------------------------------
    # cat_jpas_all_hdu     = pyfits.PrimaryHDU(cat_jpas_all)    # We create a PrimaryHDU object to encapsulate the data
    # cat_jpas_all_hdulist = pyfits.HDUList([cat_jpas_all_hdu]) # We then create a HDUList to contain the newly created
    #                                                           # primary HDU, and write to a new file
    # cat_jpas_all_hdulist.writeto(os.path.join(results_path, 'photocat_allredshifts_JPAS_fnu.fits'))
    #
    # cat_jpas_sdss_hdu     = pyfits.PrimaryHDU(cat_jpas_sdss)
    # cat_jpas_sdss_hdulist = pyfits.HDUList([cat_jpas_sdss_hdu])
    # cat_jpas_sdss_hdulist.writeto(os.path.join(results_path, 'photocat_sdss_JPAS_fnu.fits'))
    #
    # cat_jplus_all_hdu     = pyfits.PrimaryHDU(cat_jplus_all)
    # cat_jplus_all_hdulist = pyfits.HDUList([cat_jplus_all_hdu])
    # cat_jplus_all_hdulist.writeto(os.path.join(results_path, 'photocat_allredshifts_JPLUS_fnu.fits'))
    #
    # cat_jplus_sdss_hdu     = pyfits.PrimaryHDU(cat_jplus_sdss)
    # cat_jplus_sdss_hdulist = pyfits.HDUList([cat_jplus_sdss_hdu])
    # cat_jplus_sdss_hdulist.writeto(os.path.join(results_path, 'photocat_sdss_JPLUS_fnu.fits'))

    ## csv version -----------------------------------------------------------------------------------------------------
    cat_jpas_all   = pd.DataFrame(cat_jpas_all)
    cat_jpas_sdss  = pd.DataFrame(cat_jpas_sdss)
    cat_jplus_all  = pd.DataFrame(cat_jpas_all)
    cat_jplus_sdss = pd.DataFrame(cat_jplus_sdss)
    cat_jpas_all.to_csv(os.path.join(results_path, 'photocat_allredshifts_JPAS_fnu.csv'), sep=',', header=None,
                        index=False)
    cat_jpas_sdss.to_csv(os.path.join(results_path, 'photocat_sdss_JPAS_fnu.csv'), sep=',', header=None,
                        index=False)

    cat_jplus_all.to_csv(os.path.join(results_path, 'photocat_allredshifts_JPLUS_fnu.csv'), sep=',', header=None,
                        index=False)
    cat_jplus_sdss.to_csv(os.path.join(results_path, 'photocat_sdss_JPLUS_fnu.csv'), sep=',', header=None,
                        index=False)


__author__ = 'mldantas'