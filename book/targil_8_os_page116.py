__author__ = 'Guy'

import sys
import os

DIRECTORY_NAME = 1


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
    receives directory name as a parameter
    check validity of directory
    print the content of input file
    """
    directory_name = sys.argv[DIRECTORY_NAME]
    if not os.path.isdir(directory_name):
        print 'Error - Directory not found'
    else:
        print_file(directory_name + r'\input_file.txt')
        # print_file(FILE_NAME)


if __name__ == '__main__':
    main()
