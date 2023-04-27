from collections import namedtuple
from sympy import *
from sympy.abc import x, y

C = symbols('C')

Function = namedtuple('Function', 'test solved')

functions = [
    # Function(
    #    x ** 2 - 2 * y,
    #    C * exp(-2 * pi) + x ** 2 / 2 - x / 2 + 1 / 4
    # ),
    Function(
        sin(x),
        cos(x) + C
    ),
    Function(
        (x + y) / 2,
        C * exp(x / 2) - x - 2
    ),
    Function(
        y - 2 * x / y,
        sqrt(C * exp(2 * x) + 2 * x + 1)
    ),
    Function(
        x + y,
        C * exp(x) - x - 1
    ),
    Function(
        0,
        C
    )
]
