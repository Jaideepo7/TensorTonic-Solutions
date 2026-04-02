import numpy as np

def covariance_matrix(X):
    npx = np.array(X)
    npxt = npx.transpose()
    if len(X) == 1 or npx.ndim ==1 :
        return None
    npx = npx - np.mean(npx, axis =0, keepdims = True)
    print(npx)
    npxt = npxt - np.mean(npxt, axis =1, keepdims = True)
    print(npxt)
    return 1/(len(X)-1)*(npxt@npx)
