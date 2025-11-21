# PERIOD04-Assist
Collection of scripts that assist with a research project that analyzes eclipsing binary systems using PERIOD04. 

## remove_nans.py
This script removes NaN values from a TEXT file. It uses the pandas library to read a TEXT file containing time and flux/magnitude data that are tab separated with NaN values in some rows in the second column. The NaN rows are removed and a new TEXT file is created after resetting the index.
Input: 
Input: 
- filename is the name of the input TEXT file.
- dropped_nan_filename is the name of the output TEXT file.
Output:
A new TEXT file with the NaN values removed and the indices reset.
