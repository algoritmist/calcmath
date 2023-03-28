from sympy import *

from functional_progamming.fputils import Left, Right
from integrals.simpson.integral import Integral

x = symbols('x')

integrals = [
    Integral(x ** 3, (0, 1), Right(1 / 4)),
    #Integral(3 * atan(x) ** 4 / (1 + x ** 2), (-pi / 2, pi), Right(4.803684413)),
    Integral((3 * x - 1) / sqrt(2 * x ** 2 - x + 1), (-5, 10), Right(8.4176339772)),
    Integral(1 / x, (-2, 2), Left("No solution")),
    Integral(sin(x) / x, (-2, 2), Left("No solution")),
]
