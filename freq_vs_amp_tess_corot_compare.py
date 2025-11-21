"""
This script is created by Niveditha Parthasarathy
to compare frequency vs amplitude plots from 
TESS and CoRoT data.

Input:
- file1 should be the frequency vs amplitude data from TESS
- file2 should be the frequency vs amplitude data from CoRoT

Output:
- A plot comparing frequency vs amplitude from TESS and CoRoT
"""

#IMPORTING PACKAGES
import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):

    freqs = []
    amps = []


    with open(filename, "r") as f:
        for line in f:
            if line.strip() == "":
                continue
            parts = line.split()
            freqs.append(float(parts[0]))
            amps.append(float(parts[1]))

    return np.array(freqs, dtype=float), np.array(amps, dtype=float)

#filenames
file1 = "time_flux_2_exported_spec.txt"   
file2 = "lc_corot_org_exported_time_flux.txt"   

freq1, amp1 = load_data(file1)
freq2, amp2 = load_data(file2)


#plotting the amp vs freq
plt.figure(figsize=(10,6))
amp2*=-1 #one set of amplitudes is taken to be
#negative for better visualization
plt.plot(freq1, amp1, label="TESS_TF2_org", linewidth=1)
plt.plot(freq2, amp2, label="CoRoT_org", linewidth=1)

plt.xlabel("freq, 1/d")
plt.ylabel("amp")
plt.legend()
plt.grid(True)
plt.show()


#notes


"""

flux= 10**(- 0.4 * mag) 


"""