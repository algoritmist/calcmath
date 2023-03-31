from enum import Enum

from functional_progamming.fputils import Left, Either, Right
from integrals.classes.breaks import Break

inf = 1e18
class MethodType(Enum):
    LEFT = 1
    RIGHT = 2
    MIDDLE = 3
    INTERACTIVE = 4


def get_method(x):
    print(f"Resolvable break at x = {x}")
    print("Choose method of resolving")
    print("1. Left limit value")
    print("2. Right limit value")
    print("3. Average limit value")
    while True:
        i = int(input())
        if i == 1:
            return MethodType.LEFT
        if i == 2:
            return MethodType.RIGHT
        if i == 3:
            return MethodType.MIDDLE
        print("Enter value between 1 and 3:")


def is_unresolvable(f, x, eps):
    if max(abs(f(x - eps)), abs(f(x + eps))) > inf:
        return True
    if abs(f(x + eps) - f(x - eps)) > eps:
        return True
    return False


def resolve(f, x, method_type: MethodType, eps) -> Either:
    if is_unresolvable(f, x, eps):
        return Left(f"Unresolvable break at point {x}")
    if method_type is MethodType.INTERACTIVE:
        method_type = get_method(x)
    if method_type is MethodType.LEFT:
        return Right(f(x - eps))
    if method_type is MethodType.RIGHT:
        return Right(f(x + eps))
    return Right((f(x - eps) + f(x + eps)) / 2)
