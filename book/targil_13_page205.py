import math


def avg_diff(lst1, lst2):
    return math.fsum(lst1) / len(lst1) - math.fsum(lst2) / len(lst2)


def main():
    lst1 = [1, 2, 3, 4]
    lst2 = [1, 1, 1, 1]
    print avg_diff(lst1, lst2)


if __name__ == '__main__':
    main()
