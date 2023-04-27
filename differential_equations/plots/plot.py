import numpy as np
from matplotlib import pyplot as plt


def plot(f, left, right, x_data, y_data, nodes=100):
    t1 = np.linspace(left, right, nodes)
    plt.figure()
    plt.plot(t1, f(t1), 'r', label='initial function')
    t2 = np.asarray(x_data)
    plt.plot(t2, y_data, 'black', label='Euler\'s function')
    plt.legend(fontsize=14)
    plt.show()
