from abc import ABC, abstractmethod
from random import choice


class Expression(ABC):
    """
    Tree representing a mathematical expression.
    """
    def __init__(self, root=False):

        self.context = {}
        self.serialized = []
        self.parent = None
        self.root = root

    """
    Set context for variables.
    """
    def set_context(self, context):
        self.context = context

    """
    Selects a none root node randomly.
    """
    def select_node(self):
        self.serialized = self.serialize()
        node = choice(self.serialized)
        if len(self.serialized) == 1:
            return node

        while node.root:
            node = choice(self.serialized)
        return node

    """
    Gets the expression value.
    """
    @abstractmethod
    def eval(self):
        pass

    """
    Transform the tree in an array.
    """
    @abstractmethod
    def serialize(self):
        pass

    """
    Gets an array of terminal variables and constants
    """
    @abstractmethod
    def get_terminals(self):
        pass

    """
    Overrides string method.
    """
    @abstractmethod
    def __str__(self):
        pass
