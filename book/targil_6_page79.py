__author__ = 'Guy'


def list_5_members():
    """ create 5 members list
        remove all members from the beginning till the end with index jump of two
    """
    lst = [1, 2, 3, 4, 5]
    print lst
    length = len(lst)
    temp = []
    for i in xrange(1, length, 2):
        temp.append(lst[i])
    lst = temp
    print lst


def summer(lst):
    """ return the sum of all list members
    Args:
        lst - a list
    """
    summ = lst[0]
    length = len(lst)
    for i in xrange(1, length, 1):
        summ = summ + lst[i]
    return summ


def main():
    list_5_members()
    lst = [10, 11, 12, 0.75]
    print summer(lst)
    lst = [True, False, True, True]
    print summer(lst)
    lst = ['aa', 'bb', 'cc']
    print summer(lst)
    lst = [[1, 2, 3, 'a'], [4, 'b', 'c', 'd']]
    print summer(lst)


if __name__ == '__main__':
    main()
