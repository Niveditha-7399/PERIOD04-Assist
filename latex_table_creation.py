"""

This code is written by Niveditha Parthasarathy
to generate a LaTeX table having 5 columns, the last one being
empty for remarks.
the first 4 columns are: Index, Frequency, Amplitude, and Phase.

the title and label of the table can be set with the corresponding
global variables.

Input:
- main_file is the TXT document containing frequency index, frequencies, 
amplitudes, and phases.
- error_file is the TXT document containing frequency index, and the errors
associated with frequencies, amplitudes, and phases.

Output:
- latex_table.tex with the code ready to be copy pasted into
editors like Overleaf.

"""


TITLE= "Table title"
LABEL= "tab:table-label"


def cols_5():

    def read_main_file(filename):

        data = {}
        with open(filename, 'r') as f:
            for line in f:
                parts = line.split()
                if len(parts) == 4 and parts[0].startswith("F"):
                    index = parts[0]
                    freq = float(parts[1])
                    amp = float(parts[2])
                    phase = float(parts[3])
                    data[index] = (freq, amp, phase)
        return data


    def read_error_file(filename):
        errors = {}
        with open(filename, 'r') as f:
            for line in f:
                parts = line.split()
                
                if len(parts) == 4 and parts[0].startswith("F"):
                    index = parts[0]
                    #errors for frequency, amplitude and phase:
                    ef = float(parts[1])  
                    ea = float(parts[2])  
                    ep = float(parts[3])  
                    errors[index] = (ef, ea, ep)
        return errors


    def make_latex_table(main_data, error_data, output_file="latex_table.tex"):


        latex = []
        latex.append(r"\renewcommand{\arraystretch}{1.1}")
        latex.append(r"\begin{table}[ht]")
        latex.append(r"    \centering")
        latex.append(r"    \setlength{\belowcaptionskip}{1em}") 
        latex.append(r"   \caption{"+f"{TITLE}"+"}")
        latex.append(r"    \label{table:"+f"{LABEL}"+"}")
        latex.append(r"    \begin{tabular}{lcccc}")
        latex.append(r"    \toprule \\[-0.7em]")
        latex.append(r"    \textbf{Index} & \textbf{Frequency} & \textbf{Amplitude} & \textbf{Phase} & \textbf{Remarks} \\")
        latex.append(r"    \midrule \\[0.2em] ")

        for key in sorted(main_data.keys(), key=lambda x: int(x[1:])):
            f, a, p = main_data[key]
            ef, ea, ep = error_data[key]

            index_num = key[1:]                   
            #for subscripts for F:
            latex_index = f"$f_{{{index_num}}}$"  

       
            latex.append(
        f"    {latex_index} & "
        f"${f:.6f} \\pm {ef:.6f}$ & "
        f"${a:.6f} \\pm {ea:.6f}$ & "
        f"${p:.6f} \\pm {ep:.6f}$ & "
        r" \\"
    )


        latex.append(r"    \bottomrule")
        latex.append(r"    \end{tabular}")
        latex.append(r"\end{table}")

        #Writng to the file
        with open(output_file, "w") as f:
            f.write("\n".join(latex))

        print(f"LaTeX table written to {output_file}")

    ################### MAIN

    main_file = "191125-1_freqs_amps_phas.txt"      
    error_file = "191125-1_errors.txt"   

    main_data = read_main_file(main_file)
    error_data = read_error_file(error_file)

    make_latex_table(main_data, error_data)
    return None


cols_5()