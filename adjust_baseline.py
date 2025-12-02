"""
This scripted is created by Niveditha Parthasarathy
to remove long term trends that move the light curve away
from the baseline using the lightkurve package.
It uses a Savitzky–Golay filter to fit any such trends
and then remove it. If there are any misidentified trends 
from missing datapoints, use 'time_intervals_to_not_consider'
variabble to create a mask exclusing those regions from
the determination of the trends.

The window length is set to 401 like they do in the website tutorial 
https://heasarc.gsfc.nasa.gov/docs/tess/LightCurve-object-Tutorial.html

Input:
- input_filename is the name of the FITS file containing the light ccurve data.
- output_filename is the name of the file to save the FITS file with the flattened data.
- window_length is the length of the filter window (this should be an odd integer).
- plots_folder is the name of the folder where PNG files (plots) should be saved.
- fits_folder is the name of the folder where the FITS files should be saved.

Output:
- A PNG file with the plot showing the flat and original light curves. It is saved in the plots_folder.
- A FITS file with the flattened light curve data. It is saved in the fits_folder.
"""


#IMPORTING PACKAGES
import lightkurve as lk
import matplotlib.pyplot as plt
import os
from astropy.table import Table
#The input files plus the output file name
input_filename = 'hlsp_qlp_tess_ffi_s0074-0000000372759279_tess_v02_llc.fits'
flat_filename = input_filename + 'flat.fits'
plots_folder = 'detrend_lightkurve_021225_plots'
fits_folder = 'detrend_lightkurve_021225_fits'
os.makedirs(plots_folder, exist_ok=True)
os.makedirs(fits_folder, exist_ok=True),


output_filename = os.path.join(fits_folder, flat_filename)
window_length = 401 

#for saving the plots with this name
label=input_filename[18:23]
print(f"Processing file: {label}")

print(f"The data is loaded from: {input_filename}")
lc_file = lk.read(input_filename)

#remove any nans
lc = lc_file.remove_nans()

#quality==0 implies good data
lc_good_quality = lc[lc.quality == 0] 

#plotting the original data as read from the fits file
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
lc_good_quality.plot(ax=plt.gca(), label='Original SAP Flux (Quality=0)', marker='.', markersize=2)
plt.title("Original Light Curve (Before Flattening)")
plt.grid(True)


#here I will flatten the light curve so that there is no trend away from the baseline
#I exclude these intervals from the 'detrending' as the 'trends' detected here are due to missing data points
#and not the real fluctutions in the lc
time_intervals_to_not_consider = (lc_good_quality.time.value > 3318.7) & (lc_good_quality.time.value < 3319.8) |  (lc_good_quality.time.value > 3339.1) 

#Only the baseline is considered for the flattening
#^also excluding any masks set above
mask = (lc_good_quality.flux < 0.97) | time_intervals_to_not_consider

#return_trend=True for plotting purposes
flat_lc, trend_lc = lc_good_quality.flatten(
    window_length=401,
    return_trend=True,
    mask=mask
)

#Orginal data nad the flattened lc data overlaid in this plot
trend_lc.plot(ax=plt.gca(), color='r', linewidth=2, label='Fitted Trend')
plt.legend()

plt.subplot(2, 1, 2)
flat_lc.plot(ax=plt.gca(), label='Flattened Flux', marker='.', markersize=2, color='g')
plt.axhline(1.0, color='k', linestyle='--', linewidth=1, label="Normalized Baseline (1.0)")
plt.title("Flattened Light Curve (Detrended)")
plt.ylim(flat_lc.flux.min() * 0.99, flat_lc.flux.max() * 1.01) 
plt.grid(True)
plt.legend()

plt.tight_layout()


plot_path = os.path.join(plots_folder, f'flattened_lightcurve_{label}.png')
plt.savefig(plot_path, dpi=300)
plt.show()
print(f"Plot for the removing of trend saved to: {plot_path}")

#writing this flattened data into a new fits file for further analysis
tbl = Table([flat_lc.time.value, flat_lc.flux.value], names=("TIME", "FLUX"))
tbl.write(output_filename, format="fits", overwrite=True)

print(f"fits file after remmmoving trend saved to: {output_filename}")


