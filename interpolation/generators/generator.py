from math import cos, pi

import numpy as np
def generate_y_data(f, xs, noise):
    if noise:
        l, r = xs[0], xs[-1]
        return [-f(l) * 3] + [f(x) for x in xs[1:-1]] + [-f(r) * 3]
    return [f(x) for x in xs]


def generate_range(a, b, nodes=20, linspace=True):
    if linspace:
        return generate_linspace(a, b, nodes)
    return generate_chebyshev(a, b, nodes)


def generate_linspace(a, b, nodes=20):
    return np.linspace(a, b, nodes)


def generate_chebyshev(a, b, nodes=20):
    x = []
    for i in range(nodes + 1):
        ksi = -cos((2 * i + 1) / (2 * nodes + 2) * pi)
        x.append((a + b) / 2 + (b - a) / 2 * ksi)
    return x
