import numpy as np

def matrix_inverse(A):
    npa = np.array(A)
    if npa.ndim == 1 or npa.shape[0]!=npa.shape[1] or abs(np.linalg.det(npa))<10**(-7):
        return None
    return np.linalg.inv(npa)