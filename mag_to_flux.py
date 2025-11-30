"""

This codde is written by Niveditha Parthasarathy
to read a light curve TXT file with time and 
magnitude data, then convert the magnitudes to flux 
and enter this data as time and flux into a new TXT file.

Input:
- input_file is the name of the TXT file with time and magnitude data.
- output_file is the name of the output TXT file that will have the time and flux data.



"""

input_file = "lc_corot_omc.txt"     
output_file = "lc_corot_omc_flux_converted.txt"  


with open(input_file, "r") as f:
    lines = f.readlines()

with open(output_file, "w") as f:
    for line in lines:
        if line.strip():  
            parts = line.split()
            time = float(parts[0]) 
            mag = float(parts[1])

            #formiula that converts magnuiude to flux
            flux= 10**(- 0.4 * (mag))
            f.write(f"{time:.8f} {flux} \n")