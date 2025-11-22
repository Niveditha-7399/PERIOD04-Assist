# PERIOD04-Assist
Collection of scripts that assist with a research project that analyzes eclipsing binary systems using PERIOD04. 

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

## add_tmin.py

This script is used to offset the time values in a given TXT file by t_0 or t_min amount.

Input: 
- input_file is the name of the input TXT file, with three columns. Time data is in the first column.
- output_file is the name of the output TXT file.
- offset is the value to be added to each time entry.

Output:
- The output will contain the updated time values in the first column, while the other two columns remain unchanged.

## freq_vs_amp_tess_corot_compare.py
This script is used to compare frequency vs amplitude plots from TESS and CoRoT data.

Input:
- file1 should be the frequency vs amplitude data from TESS
- file2 should be the frequency vs amplitude data from CoRoT

Output:
- A plot comparing frequency vs amplitude from TESS and CoRoT

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


