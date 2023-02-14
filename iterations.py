import numpy as np


# solve Ax = b with the method of simple iterations
def solve(A, b, delta):
    alpha, beta = None, None
    if check(A):
        alpha, beta = to_iterative(A, b)
    else:
        if det(A) != 0:
            A, b = transform(A, b)
            print(b)
            if check(A):
                alpha, beta = to_iterative(A, b)

    if alpha is None or beta is None:
        return [], False
    return steps(alpha, beta, delta), True


# Ax = b => x = beta + alpha * x
def to_iterative(A, b):
    alpha, beta = A, b

    for i in range(len(A)):
        const = 0
        diag1 = A[i, i] + const
        diag2 = -const
        beta[i] = b[i] / diag1
        for j in range(len(A)):
            alpha[i, j] = -diag2 / diag1 if i == j else -A[i, j] / diag1
    return alpha, beta


# if det A != 0, try to get iterative form immediately
def transform(A, b):
    if det(A) == 0:
        return A, b
    mul = np.vectorize(lambda x: 1e-6 * x)
    eps = mul(np.random.rand(len(A), len(A)))
    inv = np.linalg.inv(A)
    mult = np.add(inv, eps)
    return np.matmul(mult, A), np.squeeze(np.asarray(np.matmul(mult, b)))


# check if |Aii| > sum (Aij)
def check(A):
    to_abs = np.vectorize(lambda x: abs(x))
    a = to_abs(A)
    for row in range(len(a)):
        row_sum = np.sum(a[row])
        if 2 * a[row, row] > row_sum:
            continue
        return False
    return True


# calculate xs
def step(alpha, beta, xs, delta):
    doubles = zip(alpha, beta)
    change = False
    x = list(map(lambda t: t[1] + np.sum(t[0].dot(xs)), doubles))
    for i in range(len(x)):
        if abs(x[i] - xs[i]) < delta:
            continue
        change = True
    return np.asarray(x), change


def steps(alpha, beta, delta):
    x = beta  # initial iteration
    while True:
        x, change = step(alpha, beta, x, delta)
        if not change:
            return x


# calculate the determinant of matrix
def det(a):
    return np.linalg.det(a)
