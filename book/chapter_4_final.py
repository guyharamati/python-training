__author__ = 'Guy'


def main():
    num = raw_input("Please enter a 5 digit number\n")
    message = 'You entered the number: '
    print '{}{}'.format(message, num)
    int_num = int(num)
    first = int_num % 10
    second = int_num / 10 % 10
    third = int_num / 100 % 10
    fourth = int_num / 1000 % 10
    fifth = int_num / 10000 % 10
    sum = first + second + third + fourth + fifth
    message = 'The digits of this number are: '
    print '{}{},{},{},{},{}'.format(message,fifth, fourth, third, second, first)
    message = 'The sum of the digits is: '
    print '{}{}' .format(message,sum)


if __name__ == '__main__':
    main()
