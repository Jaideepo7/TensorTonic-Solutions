import numpy as np

def expected_value_discrete(x, p):
    npx = np.array(x)
    npp = np.array(p)
    if not np.isclose(np.sum(npp), 1.0):
        raise ValueError("probabilities dont sum upt 1")
    arrex= npx*npp
    ex = np.sum(arrex)
    return ex 
