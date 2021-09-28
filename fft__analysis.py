import numpy as np
from colorama import Fore   #For setting color of the printed messages.
                            
def LSanalysis(filename, TDON, start, stop, tolerance):    #This is the function for single file fft analysis with fraction of data. Input filename as string, TDO name as string, start & stop value of the field and tolerance level (difference btw actual data and detrander fit function).
    
    from fit import quadfit as qf
    from matplotlib.pyplot import plot
    from matplotlib import pyplot as plt
    import numpy as np
    import scipy.signal as signal

    result=[]    #List of result and generated data. Format: [Success(True or False), Field, Channel data, Inverse Field, Detrended data, Frequency, Power Spectrum, Fourier Spectrum].
    result.extend([True])    # If Success: initially True.
    
    split(filename, 'Field', result); split(filename, TDON, result)  #This will split and store the field and TDO data and store in result list as two array entries.
    if not result[0]:    #If split failed and Success is False then raise a message and abort.
        print(Fore.RED +"abort")
        return result
    
    data=np.array([[result[1][i],result[2][i]] for i in range(len(result[1]))])    #A array of format [[Field[i], Channel output[i]]].
    
    data=np.array(sorted(data,key=lambda data:data[0])) #Sorting the two-dimensional data using Field as key.

    result[1]=np.array(data[:,0])    #Passing sorted Field to replace corresponding previous values in result.
    result[2]=np.array(data[:,1])    #Passing corresponding channel output to replace corresponding previous values in result.
    
    i=0
    while i<len(result[1]):          #Removes Field values outside the range [start, stop], and corresponding channel outputs.
        if result[1][i]<start or result[1][i]>stop:
            result[1]=np.delete(result[1],i)
            result[2]=np.delete(result[2],i)
            continue
        
        i+=1
    
    try:
        if result[1].min()>start+0.1:    #if minimum field in the file is larger than the start value, raise message and exit.
            print(Fore.RED +"Minimum value in the file is ", result[1].min())
            result[0]=False
            return result
        if result[1].max()<stop-0.1:     #if maximum field in the file is smaller than the stop value, raise message and exit.
            print(Fore.RED +"Maximum value in the file is ", result[1].max())
            result[0]=False
            return result
      
    except Exception:        #If no datapoints in the given range, raise message and exit.
            print(Fore.RED +"No good data in the range.")
            result[0]=False
            return result
        
    result.append(1.0/result[1])    #Passing an array of inverse field as the fourth element (list index 3) of list 'result'.
    
    plot(result[1], result[2])      #Plotting the channel output vs field.
    plt.show()
    
    modify(result, tolerance)    #This will change the TDO values by substracting the fifth order fit function from the original data.
   
    result[-1]=np.array(result[-1])    #Not necessary, but I'd prefer everything in array.
    
    if not result[0]:            #If 'modify' was unsuccessful, exit.
        print(Fore.RED +"abort")
        return result
    
    plot(result[1], result[4])    #Plot Modified output vs Field.
    plt.show()
    
    result.append(np.linspace(100, 502655, 5000))        #Creating temporary angular frequency array,
    
    try:
        result.append(abs(signal.lombscargle(result[3], result[4], result[5], normalize=False)))  #Power spectrum for non uniform data: least square transform.
    except Exception:    #If power spectrum transform failed, exit.
        print(Fore.RED +"Could not perform power spectrum transform.")
        result[0]=False
        return result
    
    result[5]=result[5]/(2*np.pi)    #Change angular frequency to frequency.
    
    result.append(np.sqrt(result[6]))    #Store square root of the power spectrum as the fourier spectrum.
    
    return result
    
    
    
def split(File, Parameter, result):
    
    result.append([])    #Add a list to the result to store the splitted value.
    
    with open(File) as f:        #Open and read the file.
        for line in f:           #Read out the parameters in the file (ignoring other initial information).
            if line[0:4].upper()=="TIME":
                line=line.split()
                allparameters=[i[0:4].upper() for i in line]    #Store only first four letters in capital in allparameters.
                print(allparameters)
                break
        
        try:    #Find the index of the required parameter in allparameters.
            i=allparameters.index(Parameter[0:4].upper())
        except Exception:    #If parameter wasn't found, raise message and exit.
            print(Fore.RED +"Check the parameter name with the data file.")
            result[0]=False
            return      
        
        Array=[]    #Temporary data storage.
        
        for line in f:    #Split the required parameter data and store in Array.
            line=line.split()
            Array.append(float(line[i]))
            
    result[-1]=Array    #Return Array as the last element of the list 'result'.
            
            
def inverse(Array,Returnarray): #This will inverse the field value and store it in a list. (#No use of it now)
    for i in Array:
        Returnarray.append(1/i)
        
        
def modify(result, tolerance):  #This will change the TDO values by substracting the fourth order polynomial fit data from the original.
    
    from fit import pentafit as pf
    
    try:    #Try fifth order polynomial as fit function.
        fit=pf(result[3],result[2])
        
    except Exception:     #If failed to fit, raise message and return.
        print(Fore.RED +"Modify could not detrend the data: Fitting failure.")
        result[0]=False
        return
    
    result.append([])    #Append a list to store modified channel output.
    
    def f(x,A,B,C,D,E,F):    #Fit function.
        return A*x**5 + B*x**4 + C*x**3 + D*x**2 + E*x + F
    
    i=0
    
    while i<len(result[3]):
        temp=float(result[2][i]-f(result[3][i],fit[0],fit[1],fit[2],fit[3],fit[4],fit[5]))    #Temporary modified data.
        
        if abs(temp)>tolerance:    
            for j in [1,2,3]:    #If modified data value is larger than the tolerance level, delete corresponding field, inv. field and raw data from result.
                result[j]=np.delete(result[j],i)
            
            continue
        
        result[-1].append(temp)
        i+=1

        
        
def plt(Name, TDON, Start, Stop):    #Currently not in use.
    
    from matplotlib.pyplot import plot
    
    Field=[]; TDO=[]; data=[]
    split(filename,'Field',Field);split(filename,TDON,TDO)
    
    for i in range(len(Field)):
        data.append([Field[i],TDO[i]])  
    
    data=sorted(data,key=lambda data:data[0])
    
    plot.xlim(start,stop)
    plot(data[0],data[1])
    
    
    
def aaverage(avg,*args):    #Currently not in use.
    for i in range(len(args[1])):
        x=0.0
        for j in range(len(args)):
            x+=args[j][i]
        
        avg.append(x/len(args))
        
        
        
def gaverage(avg,*args):    #Currently not in use.
    import numpy as np
    
    y=0
    for i in range(len(args[1])):
        x=1
        for j in range(len(args)):
            x=x*args[j][i]
        
        avg.append(np.power(x,1/len(args)))
