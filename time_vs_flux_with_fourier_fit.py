"""
this code reads a text file with time and flux data,
and plots the flux as a function of time. Then, it
fits a sine wave (fourier) using the data from another text file 
with data arranged as follows:
F1	0.132873199944689	 0.00607471670398125 	 0.774073550773877 
F2	0.288216710761312	 0.0018437020642556 	 0.0528653621299045 
where the first column is the frequency index, 
second column is the frequency, third column is the amplitude,
and the fourth column is the phase.

The sine wave should be of the form:
fitt= z + sum of all (Amplitude * np.sin( (2*pi) * (frequency * time) + phase )) 
(fourier transform) and the value of z is set from PERIOD04.

Input:
- data1 is the TXT file containing the time and flux data.
- data2 is the TXT file with the frequency index, frequency, amplitude, and phase data.

Output:
- A plot of flux vs time with the Fourier fit overlaid.
"""




#IMPORTING PACKAGES
import numpy as np
import matplotlib.pyplot as plt

#zero-point correction value from PERIOD04
z = 0.001277348

#file with time and flux data
data1="time_flux_191125_masked_droped_nan_det_5.txt"
data = np.loadtxt(data1)
time = data[:,0]
flux = data[:,1]

#file with index, frequency, amplitude, and phase data
data2="191125-1_freqs_amps_phas.txt"
freq_data = np.loadtxt(data2, usecols=(1,2,3))

frequencies = freq_data[:,0]
amplitudes  = freq_data[:,1]
phases      = freq_data[:,2]


fit = np.zeros_like(time) + z

for f, A, ph in zip(frequencies, amplitudes, phases):
    fit += A * np.sin((2*np.pi)*(f * time + ph))

plt.figure(figsize=(10,6))

plt.scatter(time, flux, s=18, marker='x', color='black',label="Observed Data", alpha=0.8)
plt.plot(time, fit, color='red', linewidth=2, label="Fit")

plt.xlabel("Time")
plt.ylabel("Flux")
plt.title("Flux vs Time with Fit")
#plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()

