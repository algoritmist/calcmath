import numpy as np

from interpolation.generators.generator import generate_linspace
import matplotlib.pyplot as plt

from interpolation.lagrange.solver import interpolate_list


def plot(f, left, right, x_data, y_data, nodes=100):
    t1 = generate_linspace(left, right, nodes)
    plt.figure()
    plt.plot(t1, f(t1), 'r', label='initial function')
    t2 = np.asarray(x_data)
    lagrange_points = interpolate_list(x_data, y_data, t1)
    plt.plot(t2, y_data, 'bo', label='starting points')
    plt.plot(t1, lagrange_points, 'black', label='interpolated function')
    plt.legend(fontsize=14)
    plt.show()
