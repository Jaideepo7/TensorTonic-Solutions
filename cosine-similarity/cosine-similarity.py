import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    npa = np.array(a)
    npb = np.array(b)
    npdot = np.dot(npa,npb)
    npnorm = np.linalg.norm(npa)*np.linalg.norm(npb)
    if npnorm ==0:
        return (0.0)
    else:
        return (npdot/(npnorm))
