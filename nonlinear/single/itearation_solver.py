from scipy.misc import derivative

from functional_progamming.fputils import Left, Right


def solve(f, eps, a, b, max_iters):
    if f(a) * f(b) > 0:
        return Left(f"System doesn't have a solution on [{a};{b}]")

    phi = max(derivative(f, a), derivative(f, b))
    #if not (0 <= phi < 1):
    #    return Left(f"Convergence condition for iteration method not satisfied on [{a};{b}]")

    l = -1 / phi
    x0 = b + l * f(b)
    for i in range(max_iters):
        x = x0 + l * f(x0)
        if abs(x - x0) < eps:
            return Right((x, i + 1))
        #if phi < 0.5 and abs(x - x0) < eps:
        #    return Right((x, i + 1))
        #if abs(x - x0) < (1 - phi) / phi * eps:
        #    return Right((x, i + 1))
        x0 = x
    return Left("The equation cant be solved" ""
                f" in {max_iters} iterations")
