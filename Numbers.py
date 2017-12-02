from GeneticAlgorithm import GeneticAlgorithm


class Number(GeneticAlgorithm):
    def __init__(self, num_individuals, operators, terminals, max_depth, guess_number):
        super().__init__(num_individuals, operators, terminals, max_depth)
        self.number = guess_number

    def get_fitness(self, individual):
        return abs(individual.eval() - self.number)

