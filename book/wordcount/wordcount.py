#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

MOST_COMMON = 20

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###


def find_first(str, start, list_of_signs):
    """
  this function get a string and start/stop position and returns the first occurance of one of the signs in list_of_signs
  """
    min_index = len(str) - 1
    for sign in list_of_signs:
        index = str.find(sign, start, )
        if min_index > index:
            min_index = index
    return min_index


def find_last(str, start, stop, list_of_signs):
    """
  this function get a string and start/stop position and returns the last occurance of one of the signs in list_of_signs
  """
    max_index = start
    for sign in list_of_signs:
        index = str.rfind(sign, start, stop)
        if max_index < index:
            max_index = index
    return max_index


def read_file(filename):
    """
  a helper utility function that reads a file
  and builds and returns a word_count list for it.
  """
    list_of_signs = [' ', '-', '\n', '\n\n', '\n\n\n', '.', '--', '?', ',', '!', '(', ')', '`', '"', '*', ';', ':',
                     "\'", "_"]
    list_of_signals = [' ', '-', '\n', '\n\n', '\n\n\n', '.', '--', '?', ',', '!', '(', ')', '"', '*', ';', ':', "\'",
                       "_"]
    word_count_dict = {}
    fd_in = open(filename, 'r')
    fd_rd = fd_in.read()
    i = 0
    while i != -1:
        stop_word_address = find_first(fd_rd, i, list_of_signs)
        if stop_word_address == -1:
            break
        start_word_address = find_last(fd_rd, i, stop_word_address - 1, list_of_signals)
        word = fd_rd[start_word_address:stop_word_address:1]
        if word != '' and (word.isdigit() == False):
            word_lower = word.lower()
            if word_lower in word_count_dict:  # search in dictionary
                word_count_dict[word_lower] += 1
            else:
                word_count_dict[word_lower] = 1
        i = stop_word_address + 1
    fd_in.close()
    word_count_list = []
    for item in word_count_dict:
        word_count_list.append((item, word_count_dict[item]))
    return word_count_list


def sort_list_key(lst_tuple):
    return lst_tuple[0]


def sort_list_value(lst_tuple):
    return lst_tuple[1]


def print_words(filename):
    """
  function that counts how often each word appears in the text and prints:
  word1 count1
  word2 count2
  ...
  Print the above list in order sorted by word (python will sort punctuation to
  come before letters -- that's fine). Store all the words as lowercase,
  so 'The' and 'the' count as the same word."""
    lst = read_file(filename)
    lst.sort(reverse=False, key=sort_list_key)
    for i in xrange(0, len(lst), 1):
        print lst[i]


def print_top(filename):
    """
  a print_top(filename) which is similar
  to print_words() but which prints just the top 20 most common words sorted
  so the most common word is first, then the next most common, and so on.
  """
    lst = read_file(filename)
    lst.sort(reverse=True, key=sort_list_value)
    for i in xrange(0, MOST_COMMON, 1):
        print lst[i]
    return True


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py {--count | --topcount} file'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)


if __name__ == '__main__':
    main()
