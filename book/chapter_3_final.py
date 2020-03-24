__author__ = 'Guy'


def main():
    i = 0
    while (i <= 5):
        c = round(i, 1)
        c = c * 10
        if ((c % 10) == 0):
            print int(c / 10)
        else:
            print i
        i += 0.1


if __name__ == '__main__':
    main()
