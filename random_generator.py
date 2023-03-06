import numpy as np


def generate(n, m, multiper):
    normalize = np.vectorize(lambda x: int(multiper * x))
    return normalize(np.random.rand(n, m))


def generate_and_normalize(n):
    multiper = 1e2
    mx = generate(n, n, multiper)
    for i in range(n):
        mx[i, i] += n * multiper
    return mx
