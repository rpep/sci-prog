import functions
import numpy as np

def test_CentralDiff_sin():
    f = np.sin
    x = 0
    dfdx = np.cos

    dx_vals = 10.0**np.arange(-1, -9, -1)

    deriv = []

    for dx in dx_vals:
        deriv.append(functions.CentralDiff(f, x, dx))

    for dx, df in zip(dx_vals, deriv):
        print(dx, df)

    assert 2 == 1


 
