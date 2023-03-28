from sympy import lambdify

from functional_progamming.fputils import Either, Right
from integrals.classes.integral import Integral


def calculate(integral: Integral, resolver: Resolver, steps: int) -> Either:
    f, (a, b) = lambdify('x', integral.formula), integral.ranges

    h = (b - a) / steps
    return Right(h / 6 * (
            f(a) + f(b) +
            2 * sum([f(a + i * h) for i in range(1, steps)]) +
            4 * sum([f(a + i * h - h / 2) for i in range(1, steps + 1)])
    ))


def get_error(self):
    pass
    return self.newton_leibniz_answer - self.calculate()
