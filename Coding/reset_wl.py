#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    This program redoes the WL of the E-MILES models. The spacing is now 0.9A
    Small mistakes corrected.
    @author:  Maria Luiza L. Dantas
    @date:    2017.04.28
    @version: 0.0.2
"""

import numpy as np
import pandas as pd
import os
import fileinput

# ======================================================================================================================
# Main thread

if __name__ == '__main__':

    # Loading the datasets ---------------------------------------------------------------------------------------------
    emiles_models_path     = '/home/mldantas/Dropbox/DoutoradoIAG/Challenge/emiles_ascii'
    emiles_new_models_path = '/home/mldantas/Dropbox/DoutoradoIAG/Challenge/emiles_ascii/emiles_ascii_wlcorr'
    emiles_models_list     = np.loadtxt('/home/mldantas/Dropbox/DoutoradoIAG/Challenge/emiles_list.txt', dtype=str)
    header = ('wavelength', 'T00p0300', 'T00p0400', 'T00p0500', 'T00p0600', 'T00p0700', 'T00p0800', 'T00p0900',
              'T00p1000', 'T00p1500', 'T00p2000', 'T00p2500', 'T00p3000', 'T00p3500', 'T00p4000', 'T00p4500',
              'T00p5000', 'T00p6000', 'T00p7000', 'T00p8000', 'T00p9000', 'T01p0000', 'T01p2500', 'T01p5000',
              'T01p7500', 'T02p0000', 'T02p2500', 'T02p5000', 'T02p7500', 'T03p0000', 'T03p2500', 'T03p5000',
              'T03p7500', 'T04p0000', 'T04p5000', 'T05p0000', 'T05p5000', 'T06p0000', 'T06p5000', 'T07p0000',
              'T07p5000', 'T08p0000', 'T08p5000', 'T09p0000', 'T09p5000', 'T10p0000', 'T10p5000', 'T11p0000',
              'T11p5000', 'T12p0000', 'T12p5000', 'T13p0000', 'T13p5000', 'T14p0000')

    for each_model in emiles_models_list:
        wavelength    = np.loadtxt(os.path.join(emiles_models_path, each_model), comments='#', usecols=[0])
        all_the_rest  = np.loadtxt(os.path.join(emiles_models_path, each_model), comments='#', dtype=str)[:, 1:]
        current_model_in = os.path.join(emiles_models_path, each_model)
        current_model_out = os.path.join(emiles_new_models_path, each_model)
        new_wavelength = []
        for w in range(wavelength.size):
            if w == 0:
                new_wavelength_i = round(wavelength[w], 1)
            elif w > 0:
                previous_wavelength = wavelength[w-1]
                new_wavelength_temp = round(wavelength[w], 1)
                if new_wavelength_temp == round(previous_wavelength+0.9, 1):
                    new_wavelength_i = new_wavelength_temp
                else:
                    new_wavelength_i = round(previous_wavelength+0.9, 1)
                    print 'WL was corrected'
            new_wavelength.append(new_wavelength_i)
            # with open(current_model_out, "w") as file_out:
            #     with open(current_model_in, "r") as in_file:
            #         i = 0
            #         for line in in_file:
            #             new_line = ''
            #             new_line = line.replace(wavelength[w], '') + all_the_rest[w]
            #             i+=1
            #             file_out.write(new_line)



            # for wl, line in zip(new_wavelength, file_out):
            #     fixed_cols = line.split()
            #     print "{}\t{}\t".format(new_wavelength,)

        new_wavelength = np.array(new_wavelength)
        new_model = np.column_stack((new_wavelength, all_the_rest))
        new_model_df = pd.DataFrame(new_model)
        new_model_df.to_csv(os.path.join(emiles_models_path, os.path.splitext(each_model)[0:4][0]+'.csv'), sep=',',
                             header=header, index=False)

__author_ = 'Maria Luiza Linhares Dantas'

