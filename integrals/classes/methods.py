from enum import Enum

from integrals.classes.breaks import Break


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


def resolve(function_brake: Break, method_type: MethodType, eps=1e-6):
    f, x = function_brake.f, function_brake.x
    if method_type is MethodType.INTERACTIVE:
        method_type = get_method(x)
    if method_type is MethodType.LEFT:
        return f(x - eps)
    if method_type is MethodType.RIGHT:
        return f(x + eps)
    return (f(x - eps) + f(x + eps)) / 2
