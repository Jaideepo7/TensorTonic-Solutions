import numpy as np

def euclidean_distance(x, y):
    npx=np.array(x)
    npy=np.array(y)
    return (np.sum((npx-npy)**2))**(1/2)