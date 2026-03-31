import numpy as np

def normalize_3d(v):
    npv = np.array(v)
    if npv.ndim == 1:
        mag = np.linalg.norm(npv)
        if mag!=0:
            return npv/mag
        else:
            return npv
    mag = np.linalg.norm(npv,axis = 1,keepdims=True)
    safe_mag = np.where(mag == 0, 1, mag)
    return npv / safe_mag
print(normalize_3d([3,4,2]))
