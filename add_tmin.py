"""
This script is created by Niveditha Parthasarathy
to offset the time values in a given TXT file 
by t_0/t_min amount.

Input: 
- input_file is the name of the input TXT file, with three columns. Time data is in the first column.
- output_file is the name of the output TXT file.
- offset is the value to be added to each time entry.

Output:
- output_file will contain the updated time values in the first column,
while the other two columns remain unchanged.

"""
input_file = "tess_87forperiod04.txt"     
output_file = "tess_87forperiod04_add_tmin.txt"  

offset = 54456.99559 

with open(input_file, "r") as f:
    lines = f.readlines()

with open(output_file, "w") as f:
    for line in lines:
        if line.strip():  
            parts = line.split()

            time = float(parts[0]) + offset
            
            col2 = parts[1]
            col3 = parts[2]
            
            f.write(f"{time:.8f} {col2} {col3}\n")

