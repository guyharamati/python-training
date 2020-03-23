__author__ = 'Guy'

def main(age):
    if(age==18):
        print 'Congratulations'
    elif (age<18):
        print 'You are so Young'
    else:
        print 'We love old people'

if __name__ == '__main__':
    for i in [17,18,19]:
        main(i)