import math

from sympy import *

from functional_progamming.fputils import Left
from nonlinear.single.newton_solver import solve as newton_solve
from nonlinear.single.itearation_solver import solve as iteration_solve

x = symbols('x')

equations = [
    x ** 3 - x + 4,
    0.4 * x ** 3 - 2.5 * x ** 2 + 0.5 * x + 7,
    1 / sqrt(x) - x,
    sqrt(x) - x
]

test_ranges = [(-2, 1), (1, 4), (0.5, 2), (0, 2)]


def solve_equation(number, a, b, err, max_iters=100):
    eq = lambdify(x, equations[number])
    return ("Newton's method", newton_solve(eq, err, a, b, max_iters)), \
        ("Iterations method", iteration_solve(eq, err, a, b, max_iters))
