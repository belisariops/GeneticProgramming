from Expression import Expression


class Variable(Expression):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def eval(self):
        return self.context[self.name]

    def serialize(self):
        return [self]

    def __str__(self):
        return self.name
