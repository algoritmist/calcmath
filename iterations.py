import numpy as np
from fputils import Left, Right


# solve Ax = b with the method of simple iterations
def solve(a, b, delta):
    alpha, beta = None, None
    if is_has_convergence(a):
        alpha, beta = to_iterative_form(a, b)
    #    else:
    #        if det(a) != 0:
    #            a_transformed, b_transformed = transform(a, b)
    #           alpha, beta = to_iterative_form(a_transformed, b_transformed)

    # TODO: use Maybe
    if alpha is None or beta is None:
        return Left("LES does not satisfy the convergence conditions")
    return Right(steps(alpha, beta, delta))


# Ax = b => x = beta + alpha * x
def to_iterative_form(a, b):
    alpha, beta = a, b
    for i in range(len(a)):
        # TODO: random const
        const = 0
        diag1 = a[i, i] + const
        diag2 = -const
        beta[i] = b[i] / diag1
        for j in range(len(a)):
            alpha[i, j] = -diag2 / diag1 if i == j else -a[i, j] / diag1
    return alpha, beta


# if det A != 0, try to get iterative form immediately
# def transform(a, b):
#    if det(a) == 0:
#        return a, b
#    mul = np.vectorize(lambda x: 1e-6 * x)
#    eps = mul(np.random.rand(len(a), len(a)))
#    inv = np.linalg.inv(a)
#    mult = np.add(inv, eps)
#    # TODO: try simplifying b multiplication
#    return np.matmul(mult, a), np.squeeze(np.asarray(np.matmul(mult, b)))#


# check if |Aii| > sum (Aij)
def is_has_convergence(A):
    to_abs = np.vectorize(lambda x: abs(x))
    a = to_abs(A)
    for row in range(len(a)):
        row_sum = np.sum(a[row])
        if not (2 * a[row, row] > row_sum):
            return False
    return True


# calculate xs
def step(alpha, beta, xs, delta):
    doubles = zip(alpha, beta)
    change = False
    x = list(map(lambda t: t[1] + np.sum(t[0].dot(xs)), doubles))
    for i in range(len(x)):
        if not (abs(x[i] - xs[i]) < delta):
            change = True
            break
    return np.asarray(x), change


def steps(alpha, beta, delta):
    x = beta  # initial iteration
    iterations = 0
    while True:
        x, change = step(alpha, beta, x, delta)
        iterations += 1
        if not change:
            return x, iterations


# calculate the determinant of matrix
def det(a):
    return np.linalg.det(a)
