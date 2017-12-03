from GeneticAlgorithm import GeneticAlgorithm


class Number(GeneticAlgorithm):
    """
    Genetic programming algorithm to resolve the game 'Des chiffres et des lettres'
    """
    def __init__(self, num_individuals, operators, terminals, max_depth, guess_number):
        super().__init__(num_individuals, operators, terminals, max_depth)
        self.number = guess_number

    def get_fitness(self, individual):
        terminals = individual.get_terminals()
        terminals.sort()
        repeat_count = 0
        for i in range(len(terminals) - 1):
            if terminals[i] == terminals[i + 1]:
                repeat_count += 1
        return abs(abs(individual.eval() - self.number) + repeat_count*100)

