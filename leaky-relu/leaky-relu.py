import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    npx = np.array(x)
    npx = np.where(npx>0,npx,alpha*npx)
   
    return npx