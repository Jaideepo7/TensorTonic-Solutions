
import numpy as np
def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    nps = np.array(series)
    nps = np.diff(nps,n=order)
    return nps.tolist()