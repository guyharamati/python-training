import urllib

ADDRESS = 1


def main():
    urllib.urlretrieve(r'https://upload.wikimedia.org/wikipedia/he/thumb/c/cc'
                       r'/FF9_DIGTAL1SHEET_CHARACTER_SMOKE_GROUP2_ISR.jpg/800px'
                       r'-FF9_DIGTAL1SHEET_CHARACTER_SMOKE_GROUP2_ISR.jpg '
                       , r'C:\Users\guyha\PycharmProjects\python-training\book\fast&furious9.jpg')


if __name__ == '__main__':
    main()
