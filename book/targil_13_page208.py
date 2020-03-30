def multiply_str(str):
    return ''.join(map(lambda chr: chr + chr, str))


def main():
    str = 'Cyber'
    print multiply_str(str)
    str = 'Guy Haramati !!'
    print multiply_str(str)


if __name__ == '__main__':
    main()
