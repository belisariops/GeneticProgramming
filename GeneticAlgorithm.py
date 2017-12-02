from Operator import Operator
from abc import ABC, abstractmethod
import random


class GeneticAlgorithm(ABC):
    def __init__(self, num_individuals, functions, terminals, max_depth):
        self.functions = functions
        self.terminals = terminals
        self.max_depth = max_depth
        self.num_individuals = num_individuals
        self.population = []

    def create_individual(self, depth):
        if depth >= self.max_depth:
            return self.terminals[random.randint(0, len(self.terminals) - 1)]

        rand = random.uniform(0, 1)
        if rand <= 0.5:
            return self.terminals[random.randint(0, len(self.terminals) - 1)]

        operator = Operator(self.functions[random.randint(0, len(self.functions) - 1)], 'x')
        operator.left = self.create_individual(depth - 1)
        operator.left.parent = self
        operator.right = self.create_individual(depth - 1)
        operator.right.parent = self
        return operator

    def initialize_population(self):
        for i in range(self.num_individuals):
            self.population.append(self.create_individual(self.max_depth))

    @abstractmethod
    def get_fitness(self):
        pass

    def cross_over(self, mother, father):
        mother_copy = mother.copy()
        father_copy = father.copy()
        serialized_mother = mother_copy.serialize()
        serialized_father = father_copy.serialize()
        father_cross_point = random.randint(0,len(serialized_father) - 1)
        mother_cross_point = random.randint(0,len(serialized_mother) - 1)


