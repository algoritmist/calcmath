import math

from sympy import *
from nonlinear.single.newton_solver import solve as newton_solve
from nonlinear.single.itearation_solver import solve as iteration_solve

x = symbols('x')

equations = [
    x ** 3 + 2.28 * x ** 2 - 1.934 * x - 3.907, math.e ** x - x ** 2
]


def solve_equation(number):
    return newton_solve(lambdify(x, equations[number]), 1e-3, 1, 1.5, 100), \
        iteration_solve(lambdify(x, equations[number]), 1e-3, 1.2, 1.4, 100)
