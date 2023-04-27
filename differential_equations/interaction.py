def get_error():
    print("Enter error:")
    return float(input())


def get_ranges():
    print(f"Enter range for differential equation: ")
    a = float(input("l = "))
    b = float(input("r = "))
    return a, b


def get_function():
    print("Choose function from list above")
    from differential_equations.euler.default_functions import functions
    for i, f in enumerate(functions):
        print(f"{i + 1}. y' = {f}")
    i = int(input())
    if 1 <= i <= len(functions):
        return functions[i - 1]
    raise Exception(f"Choose value between 1 and {len(functions)}")


def get_condition(x):
    print(f"Enter y({x})")
    return float(input())


def program_info():
    return "This program solves differential equations"


import differential_equations.plots.plot as plt
from differential_equations.euler.solver import solve


def run():
    print(program_info())
    while True:
        try:
            err = get_error()
            fun = get_function()
            a, b = get_ranges()
            y_a = get_condition(a)

            x_euler, y_euler = solve(fun.test, a, b, a, y_a, err)
            plt.plot(fun.solved, a, b, x_euler, y_euler)
        except Exception as ex:
            print(ex.__str__())
