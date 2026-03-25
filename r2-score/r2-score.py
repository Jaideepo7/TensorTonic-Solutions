import numpy as np

def r2_score(y_true, y_pred) -> float:
    npy_t = np.array(y_true)
    npy_p = np.array(y_pred)
    mean_npy_t = np.mean(npy_t)
    if np.array_equal(npy_t,npy_p):
        return 1
    elif np.sum((npy_t - mean_npy_t)**2)==0:
        return 0
    else:
        
        R  = 1 - np.sum((npy_t - npy_p)**2)/np.sum((npy_t -mean_npy_t)**2)
        return R

