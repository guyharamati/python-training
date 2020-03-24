__author__ = 'Guy'


def product(num1, num2):
    """ return the product of two number
    Args:
        num1 - a number
        num2 - a number
    """
    return num1 * num2


def division(num1, num2):
    """ return the division of two number - num1/num2
        checks legal divisions
    Args:
        num1 - a number
        num2 - a number
    """
    if num2 == 0:
        return 'illegal'
    else:
        return num1 / num2


def main(num1, num2):
    print product(num1, num2)
    print division(num1, num2)


if __name__ == '__main__':
    num1 = 30
    num2 = 10
    main(num1, num2)
