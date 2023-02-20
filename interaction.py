from functools import reduce

import numpy as np

from iterations import solve

from fputils import *

def interactive_mode():
    print("Enter error: ")
    err = float(input())
    print("Enter matrix dimension: ")
    n = int(input())
    matrix = [[] for i in range(n)]
    column = [0 for i in range(n)]
    print("Enter matrix: ")
    for i in range(n):
        matrix[i] = list(map(float, input().split()))
        matrix[i], column[i] = matrix[i][:-1], matrix[i][-1]

    result = solve(np.asmatrix(matrix), np.asarray(column), err)
    if result.is_left():
        print(result.get_value())
        return
    x, iters = result.get_value()
    print(f"Solved in {iters} iterations\nx = {x}")


def file_mode():
    pass


def random_mode():
    pass


keys = [
    ("-i", "interactive mode", interactive_mode),
    ("-f", "file mode", file_mode),
    ("-r", "random generation mode (for testing)", random_mode)
]


def to_str(key):
    return key[0] + ' - ' + key[1]


def keys_to_str():
    return reduce(lambda x, y: x + to_str(y) + '\n', keys, "")


def get_info():
    program_info = "MatrixSolver - the program that solves LES with the method of simple iterations"
    keys_info = "You can use the following keys to run the program:\n" + keys_to_str()
    return program_info + '\n' + keys_info

def run_interactive():
    while True:
        interactive_mode()