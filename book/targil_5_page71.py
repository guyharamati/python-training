__author__ = 'Guy'


def factorial():
    """ return the result of 5!
    """
    return 5 * 4 * 3 * 2 * 1


def beep(s):
    """ return the string s + 'beep'
    Args:
        s - a string
    """
    return s + 'beep'


def mul_2nums(a, b):
    """ return the multiplication of a and b
        for negative results => return 0
    Args:
        a - a number
        b - a number
    """
    result = a * b

    if result < 0:
        return 0
    else:
        return result


def main(s, a, b):
    print factorial()
    print beep(s)
    print mul_2nums(a, b)


if __name__ == '__main__':
    s = 'Hello'
    num1 = 10
    num2 = 2
    main(s, num1, num2)
    num2 = -2
    main(s, num1, num2)
