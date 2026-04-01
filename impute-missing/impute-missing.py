import numpy as np

def impute_missing(X, strategy='mean'):
    npm = np.array(X)
    if strategy == 'mean':
        mean = (np.nanmean(npm,axis=0,keepdims=True))
        result = np.where(np.isnan(npm),mean,npm)
        result = np.where(np.isnan(result),0,result)
        return result
        
    elif strategy == 'median':
        median = (np.nanmedian(npm,axis=0,keepdims=True))
        result = np.where(np.isnan(npm),median,npm)
        result = np.where(np.isnan(result),0,result)
        return result
print(impute_missing([[1,np.nan],[3,5]]))