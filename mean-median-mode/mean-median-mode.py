import numpy as np
from collections import Counter

def mean_median_mode(x):
    npx = np.array(x)
    counts = Counter(npx)
    max_freq = max(counts.values())
    modes = [val for val, count in counts.items() if count == max_freq]
    mode = min(modes)
    return [np.mean(npx),np.median(npx),mode]