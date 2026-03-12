import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    npx = np.array(x)
    npy = np.array(y)
    
    return np.dot(npx,npy)