from enum import Enum


class Break:
    inf = 1e64

    def __init__(self, f, x):
        self.f = f
        self.x = x

    def is_unresolvable(self, eps=1e-9):
        f, x = self.f, self.x
        if max(abs(f(x - eps)), abs(f(x + eps))) > self.inf:
            return True
        if abs(f(x + eps) - f(x - eps)) > eps:
            return True
        return False
