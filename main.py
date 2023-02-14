from iterations import solve
import numpy as np

A = np.matrix('4 0.24 -0.08; 0.09 3 -0.15; 0.04 -0.08 4.0')
b = np.array([8, 9, 20])

print(solve(A, b, 1e-3))
