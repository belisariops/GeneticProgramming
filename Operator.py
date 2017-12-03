from Expression import Expression


class Operator(Expression):
    def __init__(self, operation, name):
        super().__init__()
        self.operation = operation
        self.name = name
        self.left = None
        self.right = None

    def eval(self):
        return self.operation(self.left.eval(), self.right.eval())

    def get_terminals(self):
        return self.left.get_terminals() + self.right.get_terminals()

    def __str__(self):
        return "(" + self.left.__str__() + ")" + str(self.name) + "(" + self.right.__str__() + ")"

    def serialize(self):
        array = [self]
        return self.left.serialize() + array + self.right.serialize()

