def interpolate_by_lagrange(x_axis, y_axis, x):
    return create_lagrange_polynomial(x_axis, y_axis)(x)


def create_lagrange_polynomial(x_values, y_values):
    polynomials = [create_row_polynomial(x_values, i)
                   for i in range(len(x_values))]

    def lagrange_polynomial(x):
        return sum([y_values[i] * polynomials[i](x)
                    for i in range(len(x_values))])

    return lagrange_polynomial


def create_row_polynomial(x_values, i):
    def create_polynomial(x):
        numerator, denominator = 1, 1
        x_i = x_values[i]
        for j, x_j in enumerate(x_values):
            if i != j:
                numerator *= x - x_j
                denominator *= (x_i - x_j)
        return numerator / denominator

    return create_polynomial


def interpolate_list(x_data, y_data, xs):
    poly = create_lagrange_polynomial(x_data, y_data)
    return [poly(x) for x in xs]