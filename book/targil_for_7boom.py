__author__ = 'Guy'

def main():
    for i in xrange(0,100,1):
        if((i%7) == 0) or (i%10==7) or ((i/10)%10==7):
            print i

if __name__ == '__main__':
        main()