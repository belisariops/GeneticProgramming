from abc import ABC, abstractmethod
from random import choice


class Expression(ABC):
    def __init__(self, root=False):
        self.context = {}
        self.serialized = []
        self.parent = None
        self.root = root

    def set_context(self, context):
        self.context = context

    def select_node(self):
        self.serialized = self.serialize()
        node = choice(self.serialized)
        if len(self.serialized) == 1:
            return node

        while node.root:
            node = choice(self.serialized)
        return node

    @abstractmethod
    def eval(self):
        pass

    @abstractmethod
    def serialize(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
