import numpy as np

def epsilon_greedy(q_values, epsilon, rng=None):
    npq = np.array(q_values)
    if rng is None:
        rng = np.random.default_rng()
    number = rng.random()
    if number <= epsilon:
        return rng.integers(len(npq))
    else:
        return np.argmax(npq)