"""
This script is created by Niveditha Parthasarathy
to convert a NPY file to TXT format.

Input: 
- npy_filename is the name of the input NPY file.
- txt_filename is the name of the output TXT file.

Output:
- A TXT file containing the data from the NPY file.

"""

#IMPORTING PACKAGES
import numpy as np

npy_filename = "new_corot_residuals.npy"
txt_filename="new_corot_residuals.txt"
data = np.load(npy_filename)

np.savetxt(txt_filename, data.T, fmt="%.5f")
