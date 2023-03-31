from typing import Tuple, List


class Integral:
    def __init__(self, function, break_points: List[float], ranges: Tuple[float, float], expected_answer):
        self.unresolvable = None
        self.value_at = None
        self.function = function
        self.break_points = break_points
        self.ranges = ranges
        self.expected_answer = expected_answer

    def __str__(self):
        return f"Integral({self.function}, {self.ranges})"

