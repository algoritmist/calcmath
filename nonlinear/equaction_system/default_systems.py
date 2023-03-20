from sympy import *

x1, x2, x3 = symbols('x1 x2 x3')

systems = [[0.1 * x1 ** 2 + x1 + 0.2 * x2 ** 2 - 0.3,
            0.2 * x2 ** 2 + x2 - 0.1 * x1 * x2 - 0.7]]


def solve_system(number, ranges, err):
    system = systems[number]
    variables = free_variables(number)
    from nonlinear.equaction_system.solver import solve
    return "Iterations method", solve(Matrix(system), variables, ranges, err, 10)


def free_variables(number):
    symbols = set()
    for eq in systems[number]:
        symbols.update(eq.free_symbols)
    return list(symbols)
