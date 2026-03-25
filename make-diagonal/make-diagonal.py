import numpy as np

def make_diagonal(v):
    diag = np.zeros((len(v),len(v)))
    for i in range(len(v)):
        diag[i][i]=v[i]
    return diag