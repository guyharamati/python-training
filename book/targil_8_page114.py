__author__ = 'Guy'
import sys
FILE_NAME = 1


def print_file(input_file):
    """
    Receives file path
    print entire file line by line
    """
    fd_in = open(input_file, 'r')
    for line in fd_in:
        print line,
    fd_in.close()


def main():
    """
    receives file name as a parameter
    print the content of that file
    """
    print_file(sys.argv[FILE_NAME])


if __name__ == '__main__':
    main()
