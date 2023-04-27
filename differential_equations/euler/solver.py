
def solve(f, a, b, x0, y0, eps, step=None):
    xs = [x0]
    ys = [y0]

    h = eps / (b - a) if step is None else step
    x, y = x0, y0
    while x < b:
        y += h * f.subs([('x', x), ('y', y)])
        x += h
        xs.append(x)
        ys.append(y)
    return xs, ys