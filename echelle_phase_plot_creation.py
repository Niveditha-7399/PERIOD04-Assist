
"""
This code is written by Niveditha Parthasarathy
to read a TXT file with frequency, amplitude and
phase data retrieved from PERIOD04 analysis with
pre-whiitening process. Then a plot of frequency vs
echelle phase is created for the given period of the
binary system.

Input:
- file is the name of the input TTXT file with the 
data arranged as follows: frequency index, frequency,
amplitude and phase. 

- period is the orbital period of the binary system.
- choice is for scaling the points with amplitude [Y/N].

Output:
- Echelle phase vs frequency plot saved as 
'echelle_phase_vs_frequency' PNG file. 
"""

#Importing packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = "lc_corot_compare.txt"

#adjust the period according to system 
#under consideration
period = 4.179747

labels = []
freqs = []
amps = []
phases = []

with open(file, "r") as f:
    for line in f:
        parts = line.split()
        if len(parts) == 4 and parts[0].startswith("F"):
            labels.append(parts[0])
            freqs.append(float(parts[1]))
            amps.append(float(parts[2]))
            phases.append(float(parts[3]))


df = pd.DataFrame({
    "Index": labels,
    "Frequency": freqs,
    "Amplitude": amps,
    "Phase": phases
})



# here I calculate the echelle phase with the 
# pulsation frequency ν, modulo the orbital period, divided by the orbital period

df["EchellePhase"] = (df["Frequency"] % period) / period

print(df)

choice=input("Do you wish to scale the points according to their amplitudes? [Y/N]: ")

if choice=='N'|'n':
    # Echelle phase plott creation 
    plt.figure(figsize=(8,6))

    plt.scatter( df["EchellePhase"],df["Frequency"], s=80, marker='o')

    plt.ylabel("Frequency (d-1)")
    plt.xlabel("Echelle Phase: freq mod orb_period / orb_period")
    plt.title("Echelle Phase vs Frequency")

    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"echelle_phase_vs_frequency", dpi=300)
    plt.show()

##################################################
# # if you wish to scale the point size
# # according to the amplitudes:
##################################################

# scaled according to the size of teh aplitudes
elif choice=='Y'|'y':

    scale_factor = 2e5
    sizes = df["Amplitude"] * scale_factor

    plt.figure(figsize=(8,6))

    plt.scatter(df["EchellePhase"], df["Frequency"],
                s=sizes,         
                marker='o',
                alpha=0.75)

    plt.ylabel("Frequency (d-1)")
    plt.xlabel("Echelle Phase: freq mod orb_period / orb_period")
    plt.title("Echelle Phase vs Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"echelle_phase_vs_frequency", dpi=300)
    plt.show()
    
else:

    print("Incorrect Input")

