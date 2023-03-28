from typing import Tuple


class Integral:
    def __init__(self, formula, ranges: Tuple[float, float], newton_leibniz_answer):
        self.formula = formula
        self.ranges = ranges
        self.newton_leibniz_answer = newton_leibniz_answer

    def __str__(self):
        return f"Integral({self.formula}, {self.ranges}, {self.newton_leibniz_answer})"
