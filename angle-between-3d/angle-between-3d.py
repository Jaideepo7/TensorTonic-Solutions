import numpy as np

def angle_between_3d(v, w):
    npv = np.array(v)
    npw = np.array(w)
    dotvw = sum(npv*npw)
    cos = dotvw/(np.linalg.norm(npv)*np.linalg.norm(npw))
    np.clip(cos, -1,1)
    return np.arccos(cos)