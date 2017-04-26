rm -rf $BEAGLE_RESULTS/fitting_example/BEAGLE-input-files
BEAGLE --fit --parameter-file /home/beagle/Coding/BEAGLE-general/params/fit_photometry_example.param

## our parameter file:
BEAGLE --fit --parameter-file /home/beagle/JPAS_Challenge/fit_photometry_malu_paula.param
