from scipy.misc import derivative

from functional_progamming.fputils import Right, Left


def solve(f, eps, a, b, max_iters):
    if f(a) == 0:
        return Right(([a], 0))
    if f(b) == 0:
        return Right(([b], 0))
    if f(a) * f(b) > 0:
        return Left(f"System doesn't have a solution on [{a};{b}]")

    x0 = None
    if derivative(f, x0=a, n=2) * f(a) > 0:
        x0 = f(a)
    elif derivative(f, x0=a, n=2) * f(b) > 0:
        x0 = f(b)
    if x0 is None:
        return Left("Cant find a good approximation, specify a more concrete range")
    for i in range(max_iters):
        der = derivative(f, x0)
        if der == 0:
            return Left("Specify a more concrete range")
        x = x0 - f(x0) / der
        if is_stop_condition_satisfied(f, x, x0, eps):
            return Right(([x], i + 1))
        x0 = x
    return Left("The equation cant be solved" ""
                f" in {max_iters} iterations")


def is_stop_condition_satisfied(f, x, x0, eps):
    if abs(x - x0) < eps:
        return True
    if abs(f(x)) < eps:
        return True
    if abs(f(x) / derivative(f, x)) < eps:
        return True
    return False
