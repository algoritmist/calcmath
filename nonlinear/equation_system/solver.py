import math

from sympy import *

from functional_progamming.fputils import Right, Left


def solve(f, variables, ranges, err, max_iters):
    x0_0 = Matrix([r[0] for r in ranges])
    x0_1 = Matrix([r[1] for r in ranges])

    W = f.jacobian(variables)

    if det(W) == 0:
        return Left("Specify more concrete ranges for the system")

    W_inv = -W.inv()
    x0 = f.subs(zip(variables, x0_0))

    for i in range(max_iters):
        L = W_inv.subs(zip(variables, x0))
        x = x0 + L * f.subs(zip(variables, x0))
        cur_err = max(abs(x - x0))
        if cur_err < err:
            return Right((list(x), i + 1))
        x0 = x
    return Left(f"System can't be solved in {max_iters} iterations")
