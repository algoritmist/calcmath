from sympy import *

from functional_progamming.fputils import Right, Left


def solve(f, variables, ranges, err, max_iters):
    x0 = Matrix([r[1] for r in ranges])
    for i in range(max_iters):
        L = -f.jacobian(variables).inv().subs(zip(variables, x0))
        x = x0 + L * f.subs(zip(variables, x0))
        if max(abs(x - x0)) < err:
            return Right((list(x), i + 1))
        x0 = x
    return Left(f"System can't be solved in {max_iters} iterations")
