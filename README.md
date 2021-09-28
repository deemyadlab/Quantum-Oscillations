# Quantum_Oscillation
We used Lomb-Scargel Periodogram to determine the freqeuncy of quantum oscillations in Lithium and Sodium. The data we collected from National High Magnetic Field Lab is unevenly spaced. We can do the Fourier Transform on the interpolated data or can do teh Lomb-Scargle.
Lomb-Scargle periodogram is proportional to square of the Fourier Transform.\
In fft_analysis.py the raw data was processed and Lomb-Scargel periodogram was performed.
In fit.py the raw file was fitted with a polynomial to make it linear.
in Fourier.py the Fourier Transform was performed
Rate.py gives the magnetic field sweeping rate, minimum and maximum magnetic field.
