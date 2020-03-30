def lst_lower(num):
    return filter(lambda num: num % 3 == 0, [i for i in range(1, num)])


def sum_num(num):
    return reduce(lambda x, y: x + y, [int(str(num)[i:i+1]) for i in range(0, len(str(num)), 1)])


def main():
    num = 104
    print 'The testing num is: {}'.format(num)
    print 'List of nums smaller than {} and dividing by 3 is: \n{}'.format(num,lst_lower(num))
    print 'Sum of digits is: {}'.format(sum_num(num))


if __name__ == '__main__':
    main()
