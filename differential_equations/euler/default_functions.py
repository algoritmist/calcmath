from collections import namedtuple
from sympy import *
from sympy.abc import x, y

c = symbols('c')

Function = namedtuple('Function', 'test solved')

functions = [
    # Function(
    #    x ** 2 - 2 * y,
    #    C * exp(-2 * pi) + x ** 2 / 2 - x / 2 + 1 / 4
    # ),
    Function(
        Add(sin(x), 0 * y),
        -cos(x) + c
    ),
    Function(
        (x + y) / 2,
        c * exp(x / 2) - x - 2
    ),
    Function(
        y - 2 * x / y,
        sqrt(c * exp(2 * x) + 2 * x + 1)
    ),
    Function(
        x + y,
        c * exp(x) - x - 1
    ),
    Function(
        Add(0 * x, 0 * y),
        Add(0 * x, c)
    )
]


def calculate_const(f, _x, _y):
    cs = solve(Add(f.subs(x, _x), -_y), c)
    if len(cs) == 0:
        raise Exception("Condition can't be satisfied")
    _c = cs[0]
    return f.subs(c, _c)
