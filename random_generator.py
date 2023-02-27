import numpy as np
def generate(n, m):
    return np.random.rand(n, m)

def generate_and_normalize(n):
    mx = generate(n, n)
    for i in range(n):
        mx[i, i] += n
    return mx