from nonlinear.equation_system.default_systems import *
from nonlinear.utils import *

test_err = 1e-6
test_iters = 100


def test():
    for i, ranges in enumerate(test_ranges):
        result = solve_system(i, ranges, test_err, test_iters)
        print(f"{systems[i]} = 0")
        show_result(result)
        print("-" * 20)
