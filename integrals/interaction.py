from functional_progamming.fputils import Right, Left
from integrals.classes.methods import MethodType
from integrals.simpson.solver import calculate
from integrals.utils import show_result


def program_info():
    return "This program calculates integrals"


def get_integral():
    from integrals.simpson.default_integrals import integrals
    print("Choose one of the following equations:")
    for i, integral in enumerate(integrals):
        # TODO: pretty print
        print(f"{i + 1}. {integral}")

    i = int(input("Enter number of integral: ")) - 1
    if 0 <= i < len(integrals):
        return Right(integrals[i])
    return Left(f"Choose number from 1 to {len(integrals)}")


def get_steps():
    return int(input("Enter number of steps: "))


def run():
    print(program_info())
    while True:
        res = get_integral()
        if res.is_left():
            print(res.get_error())
            continue
        integral = res.get_value()
        steps = get_steps()
        print(show_result(calculate(integral, steps, MethodType.INTERACTIVE)))
