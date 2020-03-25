__author__ = 'Guy'

INPUT_FILE = r'C:\guy\python\input_file.txt'
OUTPUT_FILE = r'C:\guy\python\output_file.txt'


def copy_txt_files(input_file, output_file):
    """
    Receives 2 file paths
    copy entire file line by line
    """
    fd_in = open(input_file, 'r')
    fd_out = open(output_file, 'a')
    for line in fd_in:
        fd_out.write(line)
    fd_in.close()
    fd_out.close()


def main():
    copy_txt_files(INPUT_FILE, OUTPUT_FILE)


if __name__ == '__main__':
    main()
