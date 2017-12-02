from Constant import Constant
from Operator import Operator


def main():
    tree = Operator(lambda x, y: x + y, '+')
    tree.right = Constant(1)
    tree.left = Constant(2)
    tree.left.parent = tree
    tree.right.parent = tree

    tree.serialize()
    print(tree.serialize()[2])


if __name__ == "__main__":
    main()
