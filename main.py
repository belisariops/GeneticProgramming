from Numbers import Number
from Constant import Constant
from Operator import Operator


def main():
    tree = Operator(lambda x, y: x + y, '+')

    tree2 = Operator(lambda x, y: x - y, '-')
    tree3 = Operator(lambda x, y: x * y, '*')

    const1 = Constant(1)
    const2 = Constant(2)
    const3 = Constant(3)
    const4 = Constant(4)
    const5 = Constant(5)

    alg = Number(10, [tree, tree2, tree3], [const1, const2, const3, const4, const5], 3, 8)
    alg.run(2000)


if __name__ == "__main__":
    main()
