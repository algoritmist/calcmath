from enum import Enum

from integrals.classes.breaks import Break


class MethodType(Enum):
    LEFT = 1
    RIGHT = 2
    MIDDLE = 3


def resolve(function_brake: Break, method_type: MethodType, eps=1e-9):
    f, x = function_brake.f, function_brake.x
    if method_type is MethodType.LEFT:
        return f(x - eps)
    if method_type is MethodType.RIGHT:
        return f(x + eps)
    return (f(x - eps) + f(x + eps)) / 2

