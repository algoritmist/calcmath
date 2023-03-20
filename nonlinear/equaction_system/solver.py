from sympy import *

from functional_progamming.fputils import Right, Left


def solve(f, variables, ranges, err, max_iters):
    x0_0 = Matrix([r[0] for r in ranges])
    x0_1 = Matrix([r[1] for r in ranges])

    W = -f.jacobian(variables)
    d1 = det(W.subs(zip(variables, x0_0)))
    d2 = det(W.subs(zip(variables, x0_1)))

    if d1 == 0 and d2 == 0:
        return Left("Specify more concrete ranges for the system")
    x0 = x0_0 if d1 != 0 else x0_1

    for i in range(max_iters):
        L = W.inv().subs(zip(variables, x0))
        x = x0 + L * f.subs(zip(variables, x0))
        if max(abs(x - x0)) < err:
            return Right((list(x), i + 1))
        x0 = x
    return Left(f"System can't be solved in {max_iters} iterations")
