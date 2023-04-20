from sympy import lambdify


def program_info():
    return "This program interpolates functions"


def get_ranges():
    print(f"Enter range for integral: ")
    a = float(input("l = "))
    b = float(input("r = "))
    return a, b


def get_function():
    print("Choose function from list above")
    from interpolation.lagrange.default_functions import functions
    for i, f in enumerate(functions):
        print(f"{i + 1}. {f}")
    i = int(input())
    if 1 <= i <= len(functions):
        return functions[i - 1]
    raise Exception(f"Choose value between 1 and {len(functions)}")


from interpolation.generators.generator import *
from interpolation.lagrange.solver import *


def get_noise():
    print("Add noise? Yes/No")
    if input() == "Yes":
        return True
    return False


def get_points(a, b, nodes=20):
    linspace_points = generate_linspace(a, b, nodes)
    chebyshev_points = generate_chebyshev(a, b, nodes)
    print(f"1. {linspace_points}")
    print(f"2. {chebyshev_points}")
    i = int(input())
    if i == 1:
        return linspace_points
    if i == 2:
        return chebyshev_points
    raise Exception(f"Choose value 1 or 2")


def get_nodes():
    print("Enter number of nodes: ")
    n = int(input())
    if n > 0:
        return n
    raise Exception("Enter value > 0")


def run():
    print(program_info())
    while True:
        # try:
        f = lambdify('x', get_function())
        noise = get_noise()
        a, b = get_ranges()
        nodes = get_nodes()
        x_data = get_points(a, b, nodes)
        y_data = generate_y_data(f, x_data, noise)
        import plots.plot as plt
        plt.plot(f, a, b, x_data, y_data)
    # except Exception as ex:
    #    print(ex)
