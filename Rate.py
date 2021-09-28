def rate(name):
    import numpy as np
    for i in range(1,15):
        try:
            isinstance(np.loadtxt(name,skiprows=i),np.ndarray)
        except:
             continue
    data=np.loadtxt(name,skiprows=i)   
    Field=np.zeros(len(data))
    Time=np.zeros(len(data))
    for i in range(len(data)):
        Field[i]=data[i][1]
        Time[i]=data[i][0]
    field=np.abs(Field[-1]-Field[0])
    time=(np.abs(Time[-1]-Time[0]))/60
    rate=field/time
    
    return(rate, np.min(Field), np.max(Field))
