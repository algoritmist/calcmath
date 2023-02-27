import numpy as np
from fputils import Left, Right

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching


# solve Ax = b with the method of simple iterations
def get_shuffled_row_convergence(a):
    rows = [[] for i in range(len(a))]
    for i in range(len(a)):
        rows[i] = [1 if is_convergence_satisfied(a, i, j) else 0 for j in range(len(a))]
    graph = csr_matrix(rows)
    perm = maximum_bipartite_matching(graph, perm_type='column')
    return perm


def transform(a, shuffle):
    return a[shuffle]


def solve(a, b, delta):
    alpha, beta = None, None
    # if is_has_convergence(a):
    #    alpha, beta = to_iterative_form(a, b)
    # else:
    shuffle = get_shuffled_row_convergence(a)
    if shuffle is not None:
        a_transformed, b_transformed = transform(a, shuffle), transform(b, shuffle)
        alpha, beta = to_iterative_form(a_transformed, b_transformed)

    if alpha is None or beta is None:
        return Left("LES does not satisfy the convergence condition")

    x, iterations = steps(alpha, beta, delta)
    return Right((x, iterations))


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
        if not is_convergence_satisfied(a, row, row):
            return False
    return True


def is_convergence_satisfied(a, i, j):
    to_abs = np.vectorize(lambda x: abs(x))
    matrix = to_abs(a)
    return 2 * matrix[i, j] > np.sum(matrix[i])


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
