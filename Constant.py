from Expression import Expression


class Constant(Expression):
    """
    Represents a constant node.
    """
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        return self.value

    def serialize(self):
        return [self]

    def get_terminals(self):
        return [self.value]

    def __str__(self):
        return str(self.value)
