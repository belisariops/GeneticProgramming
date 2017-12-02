from abc import ABC, abstractmethod


class Expression(ABC):
    def __init__(self):
        self.context = {}
        self.serialized = []
        self.parent = None

    def set_context(self, context):
        self.context = context

    @abstractmethod
    def eval(self):
        pass

    @abstractmethod
    def serialize(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

