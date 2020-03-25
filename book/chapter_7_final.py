__author__ = 'Guy'


def check_user_input(num):
    """Receive 5 digit number from the user
    return value -  the number
                    for error input - return False
    """
    if num.isdigit() and 10000 <= int(num) < 99999:
        return num
    else:
        return False


def print_num(num):
    message = 'You entered the number: '
    print '{}{}'.format(message, num)


def calculate_digits(num):
    """
    Args - a 5 digits number
    return - each one of the digits in the number
    """
    int_num = int(num)
    first = int_num % 10
    second = int_num / 10 % 10
    third = int_num / 100 % 10
    fourth = int_num / 1000 % 10
    fifth = int_num / 10000 % 10

    return fifth, fourth, third, second, first


def sum_num(num):
    """
    Args - a 5 digits number
    return - the sum of the digits
    """
    int_num = int(num)
    first, second, third, fourth, fifth = calculate_digits(num)
    sum_number = first + second + third + fourth + fifth
    return sum_number


def main():
    assert check_user_input('123') is False, "Not protected from short numbers"
    assert check_user_input('987654') is False, "Not protected from long numbers"
    assert check_user_input('hello') is False, "Not protected from strings"
    assert check_user_input('123.2') is False, "Not protected from float numbers"
    number = raw_input("Please enter a 5 digit number\n")
    num = check_user_input(number)
    while not num:
        number = raw_input("Please enter a 5 digit number\n")
        num = check_user_input(number)
    print_num(num)
    fifth, fourth, third, second, first = calculate_digits(num)
    message = 'The digits of this number are: '
    print '{}{},{},{},{},{}'.format(message, fifth, fourth, third, second, first)
    sum_number = sum_num(num)
    message = 'The sum of the digits is: '
    print '{}{}'.format(message, sum_number)


if __name__ == '__main__':
    main()
