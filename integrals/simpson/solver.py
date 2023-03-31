from sympy import lambdify

from functional_progamming.fputils import Either, Right, left_chain
from integrals.classes.integral import Integral
from integrals.classes.methods import MethodType, resolve


def calculate(integral: Integral, n: int, method: MethodType, eps=1e-3) -> Either:
    resolve_breakpoints(integral, method, eps)
    if len(integral.unresolvable) != 0:
        return left_chain(integral.unresolvable)

    a, b = integral.ranges

    h = (b - a) / n
    m = n // 2

    return Right(h / 3 *
                 (f(integral, a, eps) + f(integral, b, eps) +
                  4 * sum([f(integral, a + i * h, eps) for i in range(1, 2 * m, 2)]) +
                  2 * sum([f(integral, a + i * h, eps) for i in range(2, 2 * m, 2)])))


def f(integral, x, eps):
    _f, break_points = lambdify('x', integral.function), integral.break_points
    for _x in break_points:
        if abs(x - _x) < eps:
            return integral.value_at[x]
    return _f(x)


def resolve_breakpoints(integral: Integral, method: MethodType, eps):
    integral.value_at = {}
    integral.unresolvable = []
    for x in integral.break_points:
        res = resolve(lambdify('x', integral.function), x, method, eps)
        if res.is_right():
            integral.value_at[x] = res.get_value()
        else:
            integral.unresolvable.append(res)
