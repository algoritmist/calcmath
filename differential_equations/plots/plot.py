import numpy as np
from matplotlib import pyplot as plt
from sympy.abc import x


def plot(f, left, right, x_data, y_data, nodes=100):
    print(f(5))
    x1 = np.linspace(left, right, nodes)
    y1 = [f(_x) for _x in x1]
    plt.figure()
    plt.plot(x1, y1, 'r', label='initial function')
    # t2_x = np.asarray(x_data)
    # t2_y = np.asarray(y_data)
    print(x_data)
    print(y_data)
    plt.plot(x_data, y_data, 'bo', label='Euler\'s function')
    plt.legend(fontsize=14)
    plt.show()
