__author__ = 'Guy'


# note => special characters:   'aeiou'
# note => test sentence:        'ani ohev otach'
def main():
    st = raw_input("Please insert string\n")
    temp = ''
    for i in xrange(0, len(st), 1):
        if st[i] in "aeiou":
            temp = temp + st[i] + 'b' + st[i]
        else:
            temp = temp + st[i]

    print temp


if __name__ == '__main__':
    main()
