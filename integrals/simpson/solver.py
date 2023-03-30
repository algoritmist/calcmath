from math import isnan

import numpy as np
from sympy import lambdify, nan

from functional_progamming.fputils import Either, Right, Left
from integrals.classes.integral import Integral
from integrals.classes.breaks import Break
from integrals.classes.methods import MethodType
from integrals.simpson.resolver import resolve


def calculate(integral: Integral, n: int, method: MethodType) -> Either:
    f, (a, b) = lambdify('x', integral.formula), integral.ranges

    h = (b - a) / n
    m = n // 2
    p1 = [get_value(f, a), get_value(f, b)]
    p2 = [get_value(f, a + i * h) for i in range(1, 2 * m, 2)]
    p3 = [get_value(f, a + i * h) for i in range(2, 2 * m, 2)]

    r1 = resolve(p1, method)
    r2 = resolve(p2, method)
    r3 = resolve(p3, method)

    errors = []
    if r1.is_left():
        errors += r1.get_error()
    if r2.is_left():
        errors += r2.get_error()
    if r3.is_left():
        errors += r3.get_error()

    if len(errors) != 0:
        return Left(errors)

    s1, s2, s3 = r1.get_value(), r2.get_value(), r3.get_value()

    return Right(h / 3 * (sum(s1) + 4 * sum(s2) + 2 * sum(s3)))


def get_value(f, x):
    try:
        return Right(f(x))
    except Exception:
        return Left(Break(f, x))
