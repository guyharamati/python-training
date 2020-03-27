#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def sort_list_second_word(str):
    """
    :param receive element of list => string name of images in file
    help sorting list according to word number 2 in file name
    :return: string =>word number 2 in file name
    """
    stop_word = str.index('.jpg')
    return str[stop_word - 4:stop_word:1]


def read_urls(filename, key):
    """
  Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order.
  """
    lst = []
    i = 0
    fd_in = open(filename, 'r')
    fd_in_data = fd_in.read()
    while i != -1:
        stop_url_address = fd_in_data.find('.jpg', i, )
        if stop_url_address == -1:
            break
        start_url_address = fd_in_data.rfind('GET', i, stop_url_address)
        html_path = 'http://data.cyber.org.il' + fd_in_data[start_url_address + 4:stop_url_address + 4:1]
        if lst.count(html_path) == 0:  # not found in the list
            lst.append(html_path)
        i = stop_url_address + 3
    if key == 2:
        lst.sort(key=sort_list_second_word)
    else:
        lst.sort()
    print lst
    debug_file = open(r'C:\guy\python\debug_file', 'w')
    for element in lst:
        debug_file.write(element + '\n')
    debug_file.close()
    fd_in.close()
    return lst


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
    check_valid_dir = os.path.isdir(dest_dir)
    if not check_valid_dir:
        dest_dir = r'C:\guy\python'
    html_file = open(dest_dir + r'\index.html', 'w')
    i = 0
    html_file.write('<html>\n<body>\n')
    for image in img_urls:
        file_dest = dest_dir + r'\img' + '{}'.format(i) + '.jpg'
        urllib.urlretrieve(image, file_dest)
        i += 1
        html_file.write('<img src =' + file_dest + '>')
    html_file.write('</body>\n</html>\n')
    html_file.close()


def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: [--todir dir] logfile '
        sys.exit(1)

    todir = args[1]
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0],int(args[2]))

    if todir:
        download_images(img_urls, todir)
        pass
    else:
        print '\n'.join(img_urls)


if __name__ == '__main__':
    main()
