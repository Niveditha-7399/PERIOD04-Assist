"""
This script is created by Niveditha Parthasarathy
to remove NaN values from a TEXT file.

The script uses the pandas library to read
a TEXT file containing time and
flux/magnitude data that are
tab separated with NaN values in some rows
in the second column.
The NaN rows are removed and a new TEXT file 
is created after resetting the index.

Input: 
filename- This is the name of the input TEXT file.
dropped_nan_filename- This is the name of the output TEXT file.

Output:
A new TEXT file with the NaN values removed
and index reset.

"""

#IMPORTING PANDAS LIBRARY
import pandas as pd

filename = 'time_flux.txt'
dropped_nan_filename='time_flux_droped_nan.txt'
df = pd.read_csv(filename, sep='\t')

df_clean = df.dropna(subset=['Flux'])
df_clean = df_clean.reset_index(drop=True)


print(df_clean)


df_clean.to_csv(dropped_nan_filename, sep='\t', index=False)
