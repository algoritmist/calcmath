from typing import List


class Either:
    def __init__(self, left_value, right_value):
        self.left_value = left_value
        self.right_value = right_value

    def get_value(self):
        pass

    def get_error(self):
        pass

    def is_left(self):
        pass

    def is_right(self):
        pass

    @staticmethod
    def chain(xs):
        pass


class LeftValueException(Exception):
    def __init__(self, message="Trying to get value from Left"):
        self.message = message
        super().__init__(self.message)


class Left(Either):
    def __init__(self, left_value):
        super().__init__(left_value, None)

    def get_value(self):
        raise LeftValueException()

    def get_error(self):
        return self.left_value

    def is_left(self):
        return True

    def is_right(self):
        return False

    def __str__(self):
        return "Left(" + str(self.left_value) + ")"

    @staticmethod
    def chain(xs: List[Either]):
        return Left(list(map(lambda x: x.get_error(), xs)))


class RightErrorException(Exception):
    def __init__(self, message="Trying to get error from Right"):
        self.message = message
        super().__init__(self.message)


class Right(Either):
    def __init__(self, right_value):
        super().__init__(None, right_value)

    def get_value(self):
        return self.right_value

    def get_error(self):
        raise RightErrorException()

    def is_left(self):
        return False

    def is_right(self):
        return True

    def __str__(self):
        return "Right(" + str(self.right_value) + ")"

    @staticmethod
    def chain(xs: List[Either]):
        return Right(list(map(lambda x: x.get_value(), xs)))
