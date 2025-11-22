
"""
This code is written by Niveditha Parthasarathy
and is used to remove trends in flux data using polynomial
fitting.

Input:
- input_file is the name of the input file containing time and flux data.
- output_file is the name of the output file to save data after removing trends.
- degree is the degree of the polynomial to use for fitting (default is 1 for linear).
- tmin and tmax define the time interval for removing the trend (default is entire range).
- plot_file is the name of the output plot file with the original and adjusted flux.

Output:
- A text file with the detrended flux data.
- A plot showing the original flux with the polynomial used for fitting and the adjusted flux.
"""

#IMPORTING PACKAGES
import numpy as np
import matplotlib.pyplot as plt


def detrend_flux_poly(input_file, output_file, degree=1,
                      tmin=None, tmax=None, plot_file="detrend_poly_plot.png"):

    #The input file is read here
    data = np.loadtxt(input_file)
    time = data[:,0]
    flux = data[:,1]

    #It takes teh full range of data if these
    #variables are not defined/ passed into the function
    if tmin is None:
        tmin = np.min(time)
    if tmax is None:
        tmax = np.max(time)

    #removing the trend in the given range with this mask
    detrend_mask = (time >= tmin) & (time <= tmax)

    time_interval = time[detrend_mask]
    flux_interval = flux[detrend_mask]

    #fit now
    coeffs = np.polyfit(time_interval, flux_interval, degree)
    poly = np.poly1d(coeffs)
    trend = poly(time_interval)
    print(f"\nPolynomial degree {degree} fit coefficients: {coeffs}")


    trend_mean = np.mean(trend)

    flux_corrected = flux.copy()
    flux_corrected[detrend_mask] = flux_interval - trend + trend_mean


    np.savetxt(output_file, np.column_stack((time, flux_corrected)), fmt="%.10f")
    print(f"Detrended data saved to: {output_file}")


    plt.figure(figsize=(10,6))

    plt.subplot(2,1,1)
    plt.plot(time, flux, 'o', markersize=3)
    plt.plot(time_interval, trend, '-', label=f"Poly Fit (deg={degree})")
    plt.title("Original Flux + Polynomial Trend")
    plt.xlabel("Time")
    plt.ylabel("Flux")
    plt.legend()


    plt.subplot(2,1,2)
    plt.plot(time, flux_corrected, 'o', markersize=3)
    plt.title("Detrended (Mean Preserved)")
    plt.xlabel("Time")
    plt.ylabel("Corrected Flux")

    plt.tight_layout()
    plt.savefig(plot_file, dpi=200)
    plt.show()

    print(f"Plot saved as: {plot_file}")

detrend_flux_poly(
    input_file="time_flux_191125_masked_droped_nan_det_4.txt",
    output_file="time_flux_191125_masked_droped_nan_det_5.txt",
    degree=2,     
    tmin=60683.1 ,
    tmax=60688.1,
    plot_file="poly_detrend_5.png"
)



