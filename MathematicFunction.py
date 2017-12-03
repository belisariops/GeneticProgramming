from GeneticAlgorithm import GeneticAlgorithm


class MathematicFunction(GeneticAlgorithm):
    def __init__(self, num_individuals, operators, terminals, max_depth, guess_function):
        super().__init__(num_individuals, operators, terminals, max_depth)
        self.guess_function = guess_function

    def get_fitness(self, individual):
        return 0
