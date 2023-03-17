from scipy.misc import derivative

from functional_progamming.fputils import Right, Left


def solve(f, eps, x0, max_iters):
    for i in range(max_iters):
        x = x0 - f(x0) / derivative(f, x0)
        if is_stop_condition_satisfied(f, x, x0, eps):
            return Right((x, i + 1))
        x0 = x
    return Left("The system cant be solved" ""
                f"in {max_iters} iterations")


def is_stop_condition_satisfied(f, x, x0, eps):
    if abs(x - x0) < eps:
        return True
    if abs(f(x)) < eps:
        return True
    if abs(f(x) / derivative(f, x)) < eps:
        return True
    return False
