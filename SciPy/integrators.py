
import numpy as np

def trapz(func, x, steps):
    """
    func = some function of a variable.
    x = range from zero you wish to integrate over
    steps = affects the precision of the calculation. A higher number yeilds a more accurate answer.
    
    Uses trapezoidal approximation to integrate the given function over the given number.
    """
    
    N = steps
    a = 0.0
    b = float(x)
    h = (b - a) / N
    
    k = np.arange(1, N)
    I = h * (0.5 * func(a) + 0.5 * func(b) + func(a + k * h).sum())
    
    return I


def simps(func, x, steps):
    """
    func = some function of a variable.
    x = range from zero you wish to integrate over
    steps = affects the precision of the calculation. A higher number yeilds a more accurate answer. Must be a positive integer.
    
    Uses Simpson's rule to integrate the given function over the given number.
    """
    
    N = steps
    a = 0.0
    b = float(x)
    h = (b - a) / N
    
    k1 = np.arange(1, (N / 2) + 1)
    k2 = np.arange(1, N/2)
    I = (1./3.) * h * (func(a) + func(b) + 4. * func(a + (2 * k1 - 1) * h).sum() + 2. * func(a + 2 * k2 * h).sum())
    
    return I