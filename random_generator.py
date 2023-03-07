import numpy as np


def generate(n, m, mult):
    normalize = np.vectorize(lambda x: int(mult * x))
    return normalize(np.random.rand(n, m))


def generate_and_normalize(n, mult=1e2):
    mx = generate(n, n, mult)
    for i in range(n):
        mx[i, i] += n * mult
    return mx
