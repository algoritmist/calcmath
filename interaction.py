from functools import reduce

import numpy as np

from iterations import solve
from random_generator import generate_and_normalize


def interactive_mode(args):
    try:
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

        solve_and_print(matrix, column, err)
    except Exception as ex:
        print(ex.__str__())
        print("Enter the equation again...")


def solve_and_print(matrix, column, err):
    result = solve(np.asmatrix(matrix), np.asarray(column), err)
    if result.is_left():
        print(result.get_value())
        return
    x, iters = result.get_value()
    print(f"Solved in {iters} iterations\nx = {x}")


def file_mode(filenames):
    for filename in filenames:
        try:
            with open(filename, "r") as file:
                err = float(file.readline())
                n = int(file.readline())

                matrix = [[] for i in range(n)]
                column = [0 for i in range(n)]
                for i in range(n):
                    matrix[i] = list(map(float, file.readline().split()))
                    matrix[i], column[i] = matrix[i][:-1], matrix[i][-1]

                print(f"Error = {err}")
                print(f"A = {matrix}")
                print(f"b = {column}")
                solve_and_print(matrix, column, err)
        except Exception as ex:
            print("A problem occurred while solving equation")
            print(ex.__str__())


def random_mode(args, n = 20):
    matrix = generate_and_normalize(n)
    column = np.random.rand(n)
    err = 1e-6
    print(f"Error: {err}")
    print(f"A = {matrix}")
    print(f"b = {column}")
    solve_and_print(matrix, column, err)


def run_interactive(args):
    while True:
        interactive_mode(args)


keys = [
    ("-i", "interactive mode", run_interactive),
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
