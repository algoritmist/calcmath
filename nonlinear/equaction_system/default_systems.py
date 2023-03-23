from sympy import *

from functional_progamming.fputils import Left

x1, x2, x3 = symbols('x1 x2 x3')

systems = [
    [
        0.1 * x1 ** 2 + x1 + 0.2 * x2 ** 2 - 0.3,
        0.2 * x2 ** 2 + x2 - 0.1 * x1 * x2 - 0.7
    ],
    [
        x1 ** 2 + x2 ** 2 + x3 ** 2 - 1,
        2 * x1 ** 2 + x2 ** 2 - 4 * x3,
        3 * x1 ** 2 - 4 * x2 + x3 ** 2
    ]
]


# ranges = [[0, 1], [0, 1]], [[0,1] * 3]

def solve_system(number, ranges, err, max_iters=100):
    system = systems[number]
    variables = free_variables(number)
    from nonlinear.equaction_system.solver import solve
    return "Iterations method", solve(Matrix(system), variables, ranges, err, max_iters)


def free_variables(number):
    symbols = set()
    for eq in systems[number]:
        symbols.update(eq.free_symbols)
    return sorted(list(map(lambda symbol: symbol.__str__(), symbols)))
