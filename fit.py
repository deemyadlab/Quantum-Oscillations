#this takes in a set of data (xdata, ydata) and returns the best quadretic function (A*x^2+B*x+C) fit for the data (A,B,C)

def quadfit(xdata,ydata):   #Fitting xdata and ydata in quadratic form and returns a list of fitting parameter values.
    
    from scipy.optimize import curve_fit
    
    def f(x,A,B,C):
        return A*x*x+B*x+C
    
    best_vals, covar = curve_fit(f, xdata, ydata)
    return(best_vals)

def linearfit(xdata,ydata): #Fitting xdata and ydata in linear form and returns a list of fitting parameter values.
    from scipy.optimize import curve_fit
    
    def f(x,A,B):
        return A*x+B
    
    best_vals, covar = curve_fit(f, xdata, ydata)
    return(best_vals)

def qubicfit(xdata,ydata):  #Fitting xdata and ydata in qubic form and returns a list of fitting parameter values.
    from scipy.optimize import curve_fit
    
    def f(x,A,B,C,D):
        return A*x*x*x+B*x*x+C*x+D
    
    best_vals, covar = curve_fit(f, xdata, ydata)
    return(best_vals)


def tetrafit(xdata,ydata):  #Fitting xdata and ydata in qubic form and returns a list of fitting parameter values.
    from scipy.optimize import curve_fit
    
    def f(x,A,B,C,D,E):
        return A*x*x*x*x+B*x*x*x+C*x*x+D*x+E
    
    best_vals, covar = curve_fit(f, xdata, ydata)
    return(best_vals)

def pentafit(xdata,ydata):  #Fitting xdata and ydata in qubic form and returns a list of fitting parameter values.
    from scipy.optimize import curve_fit
    
    def f(x,A,B,C,D,E,F):
        return A*x*x*x*x*x+B*x*x*x*x+C*x*x*x+D*x*x+E*x+F
    
    best_vals, covar = curve_fit(f, xdata, ydata)
    return(best_vals)