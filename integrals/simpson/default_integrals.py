from sympy import *

from functional_progamming.fputils import Left, Right
from integrals.classes.integral import Integral

x = symbols('x')

integrals = [
    Integral(x ** 3, [], (0, 1), Right(1 / 4)),
    Integral((3 * x - 1) / sqrt(2 * x ** 2 - x + 1), [1 / 3], (-5, 10), Right(8.4176339772)),
    Integral(1 / x, [0], (-2, 2), Left("No solution")),
    Integral(sin(x) / x, [0], (-2, 2), Right(3.210884)),
    Integral(exp(-x ** 2), [], (0, 1), Right(0.7468)),
    Integral(1 / x + 1 / (x + 1), [-1, 0], (-2, 2), Left("No solution")),
]
