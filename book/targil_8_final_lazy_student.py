__author__ = 'Guy'

import sys
import os

DIRECTORY_NAME = 1
INPUT_FILE_NAME = 1
OUTPUT_FILE_NAME = 2


def write_solutions(fd_out, result, line, error_comment, print_error):
    if print_error == 1:
        fd_out.write(error_comment)
    else:
        if line[len(line) - 1] == '\n':
            fd_out.write(line[:len(line) - 1:] + ' = ' + str(result) + '\n')
        else:
            fd_out.write(line[:len(line):] + ' = ' + str(result) + '\n')


def solve_homework(input_file, output_file):
    """
    Receives 2 file paths
    solve math homework questions from input_file
    save the results in output_file
    checks if the operation is legal
    dill with spaces
    dill with \n or not at the end of the file
    dill with wrong file name
    """
    try:
        fd_in = open(input_file, 'r')
    except IOError:
        print ('ERROR - wrong path!!!!!!!!!!!!')
        return False
    fd_out = open(output_file, 'w')
    for line in fd_in:
        operation = line.find('+')
        if operation != -1:
            result = int(line[0:operation:1]) + int(line[operation + 1::1])
            write_solutions(fd_out, result, line, "", 0)
        else:
            operation = line.find('-')
            if operation != -1:
                result = int(line[0:operation:1]) - int(line[operation + 1::1])
                write_solutions(fd_out, result, line, "", 0)
            else:
                operation = line.find('*')
                if operation != -1:
                    result = int(line[0:operation:1]) * int(line[operation + 1::1])
                    write_solutions(fd_out, result, line, "", 0)
                else:
                    operation = line.find('/')
                    if operation != -1:
                        div_val = int(line[operation + 1::1])
                        if div_val != 0:
                            result = int(line[0:operation:1]) / div_val
                            write_solutions(fd_out, result, line, "", 0)
                        else:
                            write_solutions(fd_out, result, line, "Wrong function - can't divide by zero!\n", 1)
                    else:
                        write_solutions(fd_out, result, line, "Wrong Math Function\n", 1)

    fd_in.close()
    fd_out.close()


def main():
    """
    receives directory name as a parameter
    check validity of directory
    call function solve_homework
    """
    directory_name = sys.argv[DIRECTORY_NAME]
    if not os.path.isdir(directory_name):
        print 'Error - Directory not found'
    else:
        solve_homework(directory_name + r'\homework.txt', directory_name + r'\solutions.txt')


if __name__ == '__main__':
    main()
