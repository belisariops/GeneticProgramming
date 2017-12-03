import numpy

import matplotlib.pylab as plt
from Numbers import Number
from Constant import Constant
from Operator import Operator
from Timer import Timer


def plot_time(iterations):
    iteration = []
    time = []
    timer = Timer()
    mean_time = 0
    for i in range(iterations):
        individuals = 10
        first_operation = Operator(lambda x, y: x + y, '+')
        second_operation = Operator(lambda x, y: x * y, '*')
        operations = [first_operation, second_operation]
        values = [25, 7, 8, 100, 4, 2]
        constants = []
        for value in values:
            constants.append(Constant(value))
        depth = 3
        goal = 459
        timer.start()
        build_programs(individuals, operations, constants, depth, goal, 1000)
        value = timer.stop()
        time.append(value)
        mean_time += value
        iteration.append(i + 1)
    mean_time = mean_time / iterations
    plt.figure()
    plt.title("Tiempo Tomado en 1000 Generaciones", fontsize=20)
    plt.xlabel('Iteración')
    plt.ylabel('Tiempo (segundos)')
    plt.scatter(iteration, time, color='blue')
    plt.axhline(y=mean_time, color='r', linestyle='-')
    plt.show()


def fitness_vs_population():
    x = []
    y = []
    population = numpy.arange(10, 1010, 10)
    for pop in population:
        individuals = 10
        first_operation = Operator(lambda x, y: x + y, '+')
        second_operation = Operator(lambda x, y: x * y, '*')
        operations = [first_operation, second_operation]
        values = [25, 7, 8, 100, 4, 2]
        constants = []
        for value in values:
            constants.append(Constant(value))
        depth = 3
        goal = 459
        program = Number(individuals, operations, constants, depth, goal)
        program.run(100)
        x.append(pop)
        y.append(program.get_fitness(program.best_individual))
    plt.figure()
    plt.title("Mejor fitness según población inicial", fontsize=20)
    plt.xlabel('Población inicial')
    plt.ylabel('Fitness')
    plt.plot(x, y)
    plt.show()


def build_programs(individuals, operations, constants, depth, goal, num_iterations):
    program = Number(individuals, operations, constants, depth, goal)
    program.run(num_iterations)


def show_results(individuals, operations, constants, depth, goal, num_iterations):
    print("Creando programas")
    program = Number(individuals, operations, constants, depth, goal)
    program.run(num_iterations)
    print("El mejor programa para alcanzar {0} es: {1}".format(goal, str(program.best_individual)))
    program.plot_results()


def first_example():
    individuals = 10
    first_operation = Operator(lambda x, y: x + y, '+')
    second_operation = Operator(lambda x, y: x * y, '*')
    operations = [first_operation, second_operation]
    values = [25, 7, 8, 100, 4, 2]
    constants = []
    for value in values:
        constants.append(Constant(value))
    depth = 3
    goal = 459
    show_results(individuals, operations, constants, depth, goal, 2000)


def second_example():
    individuals = 10
    first_operation = Operator(lambda x, y: x + y, '+')
    second_operation = Operator(lambda x, y: x - y, '-')
    third_operation = Operator(lambda x, y: x / y, '/')
    fourth_operation = Operator(lambda x, y: x * y, '*')
    operations = [first_operation, second_operation, third_operation, fourth_operation]
    values = [25, 7, 8, 100, 4, 2]
    constants = []
    for value in values:
        constants.append(Constant(value))
    depth = 4
    goal = 595
    show_results(individuals, operations, constants, depth, goal, 2000)


def main():
    # First example
    first_example()

    # Second example
    # second_example()

    # Time
    # plot_time(20)

    # Fitness vs Poputaltion
    # fitness_vs_population()


if __name__ == "__main__":
    main()
