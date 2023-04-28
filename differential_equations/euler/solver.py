
def solve(f, b, x0, y0, h):
    xs = [x0]
    ys = [y0]

    x, y = x0, y0
    while x < b:
        y += h * f(x, y)
        x += h
        xs.append(x)
        ys.append(y)
    return xs, ys