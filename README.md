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

