import numpy as np

def sample_var_std(x):
    npx = np.array(x)
    return (np.var(npx,ddof=1),np.std(npx,ddof=1))