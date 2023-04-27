def solve(f, a, b, x0, y0, eps):
    xs = [x0]
    ys = [y0]

    h = eps / (b - a)
    x, y = x0, y0
    while x < b:
        y += h * f(x, y)
        x += h
        xs.append(x)
        ys.append(y)
    return xs, ys