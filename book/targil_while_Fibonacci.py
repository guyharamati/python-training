__author__ = 'Guy'

def main():
    a=0
    b=1
    while True:
        if(a<10000):
            print a
        else:
            break
        c = a
        a = a + b
        b = c


if __name__ == '__main__':
        main()