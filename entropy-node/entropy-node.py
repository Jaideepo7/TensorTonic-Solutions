import numpy as np

def entropy_node(y):
    npy = np.array(y)
    unique_values, counts = np.unique(y, return_counts=True)
    prob = counts/len(y)
    entropy = -prob*np.log2(prob)
    return (np.sum(entropy))

entropy_node([0,1,0,1])
