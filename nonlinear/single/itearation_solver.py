from scipy.misc import derivative

from functional_progamming.fputils import Left, Right


def solve(f, eps, a, b, max_iters):
    if f(a) * f(b) > 0:
        return Left(f"System doesn't have a solution on [{a};{b}]")

    da, db = derivative(f, a), derivative(f, b)
    if da == 0 and db == 0:
        return Left("Specify a more concrete range")

    l, x0 = (-1 / da, a) if da > db else (-1 / db, b)
    for i in range(max_iters):
        x = x0 + l * f(x0)
        if abs(x - x0) < eps:
            return Right((x, i + 1))
        x0 = x
    return Left("The equation cant be solved" ""
                f" in {max_iters} iterations")
