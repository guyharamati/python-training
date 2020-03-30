def anti_bi(str):
    return ''.join([str[i] for i in xrange(len(str)) if str[i] != 'b'])


def main():
    str = 'abanibi aboabach bbb'
    print anti_bi(str)


if __name__ == '__main__':
    main()
