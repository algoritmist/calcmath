import numpy as np
from matplotlib import pyplot as plt
from sympy.abc import x


def plot(f, left, right, x_data, y_data, nodes=100):
    x1 = list(np.linspace(left, right, nodes))
    y1 = [f(_x) for _x in x1]
    plt.figure()
    plt.plot(x1, y1, 'r', label='initial function')
    from interpolation.lagrange.solver import interpolate_list
    y2 = interpolate_list(x_data, y_data, x1)
    plt.plot(x_data, y_data, 'bo', label='Euler\'s function')
    plt.plot(x1, y2, 'black', label='Euler\'s function')
    plt.legend(fontsize=14)
    plt.show()
