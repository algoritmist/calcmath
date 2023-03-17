class Either:
    def __init__(self, left_value, right_value):
        self.left_value = left_value
        self.right_value = right_value

    def get_value(self):
        pass

    def is_left(self):
        pass

    def is_right(self):
        pass


class Left(Either):
    def __init__(self, left_value):
        super().__init__(left_value, None)

    def get_value(self):
        return self.left_value

    def is_left(self):
        return True

    def is_right(self):
        return False


class Right(Either):
    def __init__(self, right_value):
        super().__init__(None, right_value)

    def get_value(self):
        return self.right_value

    def is_left(self):
        return False

    def is_right(self):
        return True
