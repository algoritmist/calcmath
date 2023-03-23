from nonlinear.single.default_equations import *
from nonlinear.utils import *

test_err = 1e-6
test_iters = 100


def test():
    for i, (a, b) in enumerate(test_ranges):
        print(f"{equations[i]} = 0")
        print(f"Range [{a};{b}]")
        results = solve_equation(i, a, b, test_err, test_iters)
        show_results(results)
        print("-" * 20)
