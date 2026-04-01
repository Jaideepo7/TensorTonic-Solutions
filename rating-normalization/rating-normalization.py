import numpy as np
def rating_normalization(matrix):
    npm = np.array(matrix)
    npmnan = np.where(npm == 0, np.nan, npm)
    mean = (np.nanmean(npmnan,axis=1,keepdims=True))
    arr= np.where(npm!=0,npm-mean,0)
    return arr.tolist()
