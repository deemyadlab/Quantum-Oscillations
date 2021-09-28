def fourier(name,name1):
    import matplotlib.pyplot as plt
    import numpy as np
    import scipy
    from scipy.interpolate import interp1d

    f=scipy.interpolate.interp1d(name,name1,kind=3)
    xnew=np.linspace(name[0],name[-1],2000)
    ynew=f(xnew)
    delta=xnew[0]-xnew[1]
    freq=np.fft.fftfreq(len(xnew),delta)
    four=np.fft.fft(ynew)
    
    return  (len(name),plt.plot(freq,np.power(np.abs(four),2)))
