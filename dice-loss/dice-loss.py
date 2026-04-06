import numpy as np

def dice_loss(p, y, eps=1e-8):
    npp = np.array(p)
    npy = np.array(y)
    return 1- (2*np.sum(npp*npy)+eps)/(np.sum(npp)+np.sum(npy)+eps)