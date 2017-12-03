from copy import deepcopy, copy
from abc import ABC, abstractmethod

import matplotlib.pylab as plt
import random


class GeneticAlgorithm(ABC):
    def __init__(self, num_individuals, operators, terminals, max_depth):
        self.functions = operators
        self.terminals = terminals
        self.max_depth = max_depth - 1
        self.num_individuals = num_individuals
        self.population = []
        self.generations = []
        self.fitness = []
        self.best_individual = None

    """
    Creates individual recursively.
    """
    def create_individual(self, depth):
        if depth <= 0:
            return self.terminals[random.randint(0, len(self.terminals) - 1)]

        rand = random.uniform(0, 1)
        if rand <= 0.1:
            return self.terminals[random.randint(0, len(self.terminals) - 1)]
        operator = copy(self.functions[random.randint(0, len(self.functions) - 1)])
        operator.left = self.create_individual(depth - 1)
        operator.right = self.create_individual(depth - 1)
        return operator

    """
    Initialize population with a number of individual and max depth for each one.
    """
    def initialize_population(self):
        for i in range(self.num_individuals):
            self.population.append(self.create_individual(self.max_depth))

    """
    Calculate an individual fitness
    """
    @abstractmethod
    def get_fitness(self, individual):
        pass

    """
    Reproduce two individuals, changing sub-tress in a random node.
    """
    def cross_over(self, mother, father):
        if random.uniform(0, 1) > 0.9:
            return deepcopy(mother)

        mother_copy = deepcopy(mother)
        father_copy = deepcopy(father)
        mother_sub_tree = mother_copy.select_node()
        father_sub_tree = father_copy.select_node()
        if mother_sub_tree.parent is None:
            return mother
        if mother_sub_tree.parent.left == mother_sub_tree:
            mother_sub_tree.parent.left = father_sub_tree
        elif mother_sub_tree.parent.right == mother_sub_tree:
            mother_sub_tree.parent.right = father_sub_tree

        return mother_sub_tree.parent

    """
    Change the value of a node, with a probability.
    """
    def mutate(self, individual):
        if random.uniform(0, 1) > 0.99:
            new_individual = deepcopy(individual)
            change = new_individual.select_node()
            if change.parent is None:
                return self.create_individual(self.max_depth)
            if change.parent.left == change:
                change.parent.left = self.create_individual(2)
            elif change.parent.right == change:
                change.parent.right = change
            return change.parent
        return individual

    """
    Tournament selection
    """
    def tournament_selection(self):
        best_individual = None
        for i in range(int(self.num_individuals * 0.7)):
            individual = random.choice(self.population)
            if (best_individual is None) or (
                        self.get_fitness(individual) > self.get_fitness(best_individual)):
                best_individual = individual
        return best_individual

    """
    Execute the algorithm to create programs.
    """
    def run(self, num_iterations):
        self.initialize_population()
        best_fitness = 200000
        for i in range(num_iterations):
            child_population = []
            if best_fitness == 0:
                break
            while len(child_population) < self.num_individuals:
                mother = self.tournament_selection()
                father = self.tournament_selection()
                son = self.cross_over(mother, father)
                son = self.mutate(son)
                son_fitness = self.get_fitness(son)
                mother_fitness = self.get_fitness(mother)
                father_fitness = self.get_fitness(father)
                if son_fitness < mother_fitness and son_fitness < father_fitness:
                    child_population.append(son)
                    if best_fitness > son_fitness:
                        best_fitness = son_fitness
                        self.best_individual = son
                elif mother_fitness <= father_fitness:
                    child_population.append(mother)
                    if best_fitness > mother_fitness:
                        best_fitness = mother_fitness
                        self.best_individual = mother
                elif father_fitness < father_fitness:
                    child_population.append(father)
                    if best_fitness > father_fitness:
                        best_fitness = father_fitness
                        self.best_individual = father
            self.generations.append(i + 1)
            self.fitness.append(best_fitness)

    """
    Print on screen the mathematical function of the best individual.
    """
    def print_best_individual(self):
        print(self.best_individual)

    """
    Plot results of fitness in each generation on screen.
    """
    def plot_results(self):
        plt.figure()
        plt.title("Fitness según la generación", fontsize=20)
        plt.xlabel('Generación')
        plt.ylabel('Fitness')
        plt.plot(self.generations, self.fitness)
        plt.show()
