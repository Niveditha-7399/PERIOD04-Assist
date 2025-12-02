# PERIOD04-Assist
Collection of scripts that assist with a research project that analyzes eclipsing binary systems using PERIOD04. 

## echelle_phase_plot_creation.py
This code reads a TXT file with frequency, amplitude and phase data retrieved from PERIOD04 analysis with pre-whiitening process. Then a plot of frequency vs echelle phase is created for the given period of the binary system.

Input:
- file is the name of the input TXT file with the data arranged as follows: frequency index, frequency, amplitude and phase. 

- period is the orbital period of the binary system.
- choice is for scaling the points with amplitude [Y/N].

Output:
- Echelle phase vs frequency plot saved as 'echelle_phase_vs_frequency' PNG file. 


## fix_trends_in_range.py

This code is used to remove trends in flux data using polynomial fitting.

Input:
- input_file is the name of the input file containing time and flux data.
- output_file is the name of the output file to save data after removing trends.
- degree is the degree of the polynomial to use for fitting (default is 1 for linear).
- tmin and tmax define the time interval for removing the trend (default is entire range).
- plot_file is the name of the output plot file with the original and adjusted flux.

Output:
- A text file with the detrended flux data.
- A plot showing the original flux with the polynomial used for fitting and the adjusted flux.

## adjust_baseline.py
This scripted is created by Niveditha Parthasarathyto remove long term trends that move the light curve away from the baseline using the lightkurve package. It uses a Savitzky–Golay filter to fit any such trends and then remove it. If there are any misidentified trends from missing datapoints, use 'time_intervals_to_not_consider' variabble to create a mask exclusing those regions from the determination of the trends.

The window length is set to 401 like they do in the website tutorial https://heasarc.gsfc.nasa.gov/docs/tess/LightCurve-object-Tutorial.html

Input:
- input_filename is the name of the FITS file containing the light ccurve data.
- output_filename is the name of the file to save the FITS file with the flattened data.
- window_length is the length of the filter window (this should be an odd integer).
- plots_folder is the name of the folder where PNG files (plots) should be saved.
- fits_folder is the name of the folder where the FITS files should be saved.

Output:
- A PNG file with the plot showing the flat and original light curves. It is saved in the plots_folder.
- A FITS file with the flattened light curve data. It is saved in the fits_folder.


## time_vs_flux_with_fourier_fit.py
This code reads a text file with time and flux data, and plots the flux as a function of time. Then, it fits a sine wave (fourier) using the data from another text file with data arranged as follows:
F1	0.132873199944689	 0.00607471670398125 	 0.774073550773877 
F2	0.288216710761312	 0.0018437020642556 	 0.0528653621299045 
where the first column is the frequency index, second column is the frequency, third column is the amplitude, and the fourth column is the phase. The sine wave should be of the form: fit= z + sum of all (Amplitude * np.sin( (2*pi) * (frequency * time) + phase )) (fourier transform) and the value of z is set from PERIOD04.

Input:
- data1 is the TXT file containing the time and flux data.
- data2 is the TXT file with the frequency index, frequency, amplitude, and phase data.

Output:
- A plot of flux vs time with the Fourier fit overlaid.

## period04_fouriers_overlaid.py
This code reads four TXT files containg frequency and amplitude data from PERIOD04 analysis after the first frequency is identified, and plot this data overlaid on a frequency vs amplitude plot with alpha 0.7 to see the overlapping values.

Input:
- names of four TXT files that contain data as 'frequency' and 'amplitude' columns.

Output:
- A PNG file with the name 'overlaid_first_fouriers.png'.

## latex_table_creation.py
This code is used for generating a LaTeX table having 5 columns, the last one being empty for remarks. The first 4 columns are: Index, Frequency, Amplitude, and Phase. The title and label of the table can be set with the corresponding global variables.

Input:
- main_file is the TXT document containing frequency index, frequencies, 
amplitudes, and phases.
- error_file is the TXT document containing frequency index, and the errors
associated with frequencies, amplitudes, and phases.

Output:
- latex_table.tex with the code ready to be copy pasted into
editors like Overleaf.

## mag_to_flux.py

This code is written by Niveditha Parthasarathy to read a light curve TXT file with time and magnitude data, then convert the magnitudes to flux  and enter this data as time and flux into a new TXT file.

Input:
- input_file is the name of the TXT file with time and magnitude data.
- output_file is the name of the output TXT file that will have the time and flux data.

Output: 
- A TXT file with time and flux data.

## freq_vs_amp_tess_corot_compare.py
This script is used to compare frequency vs amplitude plots from TESS and CoRoT data.

Input:
- file1 should be the frequency vs amplitude data from TESS
- file2 should be the frequency vs amplitude data from CoRoT

Output:
- A plot comparing frequency vs amplitude from TESS and CoRoT

## add_tmin.py

This script is used to offset the time values in a given TXT file by t_0 or t_min amount.

Input: 
- input_file is the name of the input TXT file, with three columns. Time data is in the first column.
- output_file is the name of the output TXT file.
- offset is the value to be added to each time entry.

Output:
- The output will contain the updated time values in the first column, while the other two columns remain unchanged.

## remove_nans.py
This script removes NaN values from a TEXT file. It uses the pandas library to read a TEXT file containing time and flux/magnitude data that are tab separated with NaN values in some rows in the second column. The NaN rows are removed and a new TEXT file is created after resetting the index.
Input: 
- filename is the name of the input TEXT file.
- dropped_nan_filename is the name of the output TEXT file.
Output:
- A new TEXT file with the NaN values removed and the indices reset.

## convert_from_npy_to_txt.py
This script is created by Niveditha Parthasarathy to convert a NPY file to TXT format.

Input: 
- npy_filename is the name of the input NPY file.
- txt_filename is the name of the output TXT file.

Output:
- A TXT file containing the data from the NPY file.







