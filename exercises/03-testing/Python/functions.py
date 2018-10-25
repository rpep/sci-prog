import numpy as np


def squared(x):
    """
    Input:
    x, float or int
        Base value
    Output:
        float, base to the power 2.
    """
    
    return float(x) * float(x)


def pow(x, exponent):
    """
    Input:
        x: float or int
            Base value
        exponent: float or int
            Exponent value

    Output:
        float, base to the power exponent.
    """
    return float(x) ** n





def CentralDiff(f, x, dx):
    """
    Computes the 1st derivative of a function of a single variable f(x)
    by central differencing:

    \begin{equation}
    f'(x) \approx \frac{f(x + dx) - f(x - dx)}{2 * dx}
    \end{equation}

    Input:
        f: function
            Function of a single variable that returns a float
        x: 
            Point at which the derivative will be computed
        dx: 
            Step size in the central difference algorithm
    """
    return (f(x + dx) - f(x - dx)) / (2*dx)



def Newton(f, x0, tol=1e-5, dx=1e-8):
    """
    Root finding using Newton's method.
    Uses central differencing to find the derivative in the formula:

    \begin{equation}
    x_n+1 = x_n - f(x) / f'(x)
    \end{equation}
    
    Input:
        f: function
            Function of a single variable that returns a float.
        x0: Float
           Initial guess at root.
        tol: Float
           Algorithm stops when abs(x - x0) >= tol.
        dx: Float
           Step size for central differencing
    """
        

        

    x = x0 - f(x0)/CentralDiff(f, x0, dx)
    
    while(np.abs(x - x0) >=tol):
        x0 = x
        x = x0 - f(x0)/CentralDiff(f, x0, dx)

    return x



