import numpy as np

def twoPtForwardDiff(x, y):
    """
    Takes an array of values x and y and returns the derivative of y with respect to x.
    It does this by taking the average value of y between two points over the average
    value of x between two points for all points. It does this in a forward direction
    for all points but the last one, which has no point to go forward to, so that one
    is calculated seperately.
    """
    
    dydx = np.zeros(y.shape, float)            #makes dydx the same dimensions as the given y arrray
    dydx[0:-1] = np.diff(y)/np.diff(x)         #calculates the derivatives of all points but the last one
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2]) #calcualtes the derivative of the last point
    
    return dydx
    
def twoPtCenteredDiff(x, y):
    """
    Takes an array of values x and y and returns the derivatives of y with respect to x.
    It does this by taking the difference between two points above and below whichever point
    it is looking at; except for the first and last points, which have either nothing above
    or nothing below them. It calculates the first and last point induvidually.
    """
    
    dydx = np.zeros(y.shape, float)                       #makes dydx the same dimensions as the given y arrray
    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2])        #calculates the derivatives of all points but the first and last
    dydx[0] = (y[1] - y[0])/(x[1] - x[0])                 #calculates the derivative of the first point
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])            #calculates the derivative of the last point
    
    return dydx

def fourPtCenteredDiff(x, y):
    """
    Takes an array of values x and y and returns the derivatives of y with respect to x.
    More accurate than two point methods.
    """
    
    dydx = np.zeros(y.shape, float)                       
    dydx[2: -2] = (y[:-4] - (8 * y[1:-3]) + (8 * y[3:-1]) - y[4:]) / (12 *(x[4:] - x[3:-1] + x[1: -3] - x[:-4]))
    dydx[2] = (8 * y[3] - 8 * y[2]) / (12 * (x[3] - x[2]))
    dydx[1] = (8 * y[2] - 8 * y[1])/ (12 * (x[2] - x[1]))
    dydx[-2] = (8 * y[-2] - 8 *y[-3]) / (12 * (x[-2] - x[-3]))
    dydx[-1] = (8 * y[-1] - 8 * y[-2])/ 12 * ((x[-1] - x[-2]))     
    
    return dydx