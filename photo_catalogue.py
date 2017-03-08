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

# ======================================================================================================================
# Main thread

if __name__ == '__main__':

    my_data_z021   = '/home/mldantas/Dropbox/DoutoradoIAG/Challenge/total_file_z021.dat'
    my_data_z050   = '/home/mldantas/Dropbox/DoutoradoIAG/Challenge/total_file_z050.dat'
    my_data_z090   = '/home/mldantas/Dropbox/DoutoradoIAG/Challenge/total_file_z090.dat'
    my_data_sdss   = '/home/mldantas/Dropbox/DoutoradoIAG/Challenge/table_sdss_galaxies.dat'
    sdss_redshifts = '/home/mldantas/Dropbox/DoutoradoIAG/Challenge/redshifts.dat'

    galaxies_z021 = np.fromfile(my_data_z021, count=-1, dtype=float)
    galaxies_z050 = np.fromfile(my_data_z050, count=-1, dtype=float)
    galaxies_z090 = np.fromfile(my_data_z090, count=-1, dtype=float)

    with open(my_data_z021) as f:
        galaxies_z021 = f.readlines()
        galaxies_z021 = [x.strip() for x in galaxies_z021]
        # you may also want to remove whitespace characters like `\n` at the end of each line

    with open(my_data_z050) as f:
        galaxies_z050 = f.readlines()
        galaxies_z050 = [x.strip() for x in galaxies_z050]
        # you may also want to remove whitespace characters like `\n` at the end of each line

    with open(my_data_z090) as f:
        galaxies_z090 = f.readlines()
        galaxies_z090 = [x.strip() for x in galaxies_z090]
        # you may also want to remove whitespace characters like `\n` at the end of each line



    # print galaxies_z021[0:65]
    #
    #
    # exit()