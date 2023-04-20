from interpolation.lagrange.solver import interpolate_by_lagrange

x_data = [1, 5, 17]
y_data = [10, -3, 5]

x_test = [1, 5, 17, 3, 19]
for x in x_test:
    print(f"f({x}) = {interpolate_by_lagrange(x_data, y_data, x)}")