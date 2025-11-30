"""
This code is written by Niveditha Parthasarathy
to read four TXT files containg frequency
and amplitude data from PERIOD04 analysis
after the first frequency is identified,
and plot this data overlaid on a frequency vs 
amplitude plot with alpha 0.7 to see the overlapping values.

Input:
- names of four TXT files that contain data 
'frequency' and 'amplitude'.

Output:
- A PNG file with the name 'overlaid_first_fouriers.png'.

"""

#importing packages
import matplotlib.pyplot as plt
import numpy as np

#names of the input TXT files
file1='fourier_1.txt'
file2='fourier_2.txt'
file3='fourier_3.txt'
file4='fourier_4.txt'

data = np.loadtxt(file1)
freq = data[:,0]
amp = data[:,1]

data = np.loadtxt(file2)
freq2 = data[:,0]
amp2 = data[:,1]

data = np.loadtxt(file3)
freq3 = data[:,0]
amp3 = data[:,1]

data = np.loadtxt(file4)
freq4 = data[:,0]
amp4 = data[:,1]

plt.figure(figsize=(10,5))
plt.plot(freq, amp,color='red', label='1')
plt.plot(freq2, amp2,color='blue', label='2', alpha=0.7)
plt.plot(freq3, amp3,color='yellow', label='3', alpha=0.7)
plt.plot(freq4, amp4,color='green', label='4', alpha=0.7)
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("Overlaid first fouriers")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(f"overlaid_first_fouriers", dpi=300)
plt.show()


