import math

f1 = lambda num: num + 2
f2 = lambda num: math.fabs(num)


def main():
    num = 10
    print f1(num)
    lst = [2, -8, 5, -6, -1, 3]
    for i in xrange(len(lst)):
        lst[i] = int(f2(lst[i]))
    lst.sort()
    print lst


if __name__ == '__main__':
    main()
