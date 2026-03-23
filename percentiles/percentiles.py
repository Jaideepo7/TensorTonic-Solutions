import numpy as np

def percentiles(x, q):
    npx = np.array(x)
    npq = np.array(q)
    npx = np.sort(npx)
    npp = np.percentile(npx,npq,method = "linear")    
    return npp