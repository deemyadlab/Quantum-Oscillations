# Quantum_Oscillation
This code is developed to analyze the Fermiology data in which the magnetic susceptibility/electrical resistance of a sample at low temperature is measured as a function of the external magnetic field (dHvA/ SdH effects). Since the oscillations are in 1/B whereas data is collected as a function of B, we need to look at the inverse data. Furthermore the data collected in the National High Magnetic Field Lab is unevenly spaced in B. Therefore Fourier transform analysis to identify the oscillation frequencies required interpolation to make the sample spacing even in 1/B. Instead in this code we used Lomb-Scargel Periodogram to determine the frequency of quantum oscillations in the samples. Lomb-Scargle periodogram is proportional to the square of the Fourier Transform.
In fft_analysis.py the raw data was processed and Lomb-Scargel periodogram was performed.
In fit.py the raw file was fitted with a polynomial to make it linear.
in Fourier.py the Fourier Transform was performed
Rate.py gives the magnetic field sweeping rate, minimum and maximum magnetic field.
