import numpy as np
from fputils import Left, Right

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching


def get_shuffled_row_convergence(a):
    rows = [[] for i in range(len(a))]
    for i in range(len(a)):
        rows[i] = [1 if is_convergence_satisfied(a, i, j) \
                       else 0 for j in range(len(a))]
    graph = csr_matrix(rows)
    perm = maximum_bipartite_matching(graph, perm_type='column')
    return perm


def transform(a, shuffle):
    return a[shuffle]


def solve(a, b, delta):
    shuffle = get_shuffled_row_convergence(a)
    if -1 in shuffle:
        return Left("LES does not satisfy the convergence condition")
    a_transformed, b_transformed = transform(a, shuffle), \
        transform(b, shuffle)

    alpha, beta = to_iterative_form(a_transformed, b_transformed)
    x, iterations = steps(alpha, beta, delta)
    return Right((x, iterations))


def to_iterative_form(a, b):
    alpha, beta = a, b
    for i in range(len(a)):
        diag = a[i, i]
        beta[i] = b[i] / diag
        for j in range(len(a)):
            alpha[i, j] = 0 if i == j else -a[i, j] / diag
    return alpha, beta


def is_has_convergence(matrix):
    for row in range(len(matrix)):
        if not is_convergence_satisfied(matrix, row, row):
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
    x = beta
    iterations = 0
    while True:
        x, change = step(alpha, beta, x, delta)
        iterations += 1
        if not change:
            return x, iterations
