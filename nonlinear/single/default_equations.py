import math

from sympy import *
from nonlinear.single.newton_solver import solve as newton_solve
from nonlinear.single.itearation_solver import solve as iteration_solve

x = symbols('x')

equations = [
    x ** 3 - x + 4, x ** 3 + 2.28 * x ** 2 - 1.934 * x - 3.907, math.e ** x - x ** 2
]


def solve_equation(number, a, b, err):
    return newton_solve(lambdify(x, equations[number]), err, a, b, 100), \
        iteration_solve(lambdify(x, equations[number]), err, a, b, 100)
