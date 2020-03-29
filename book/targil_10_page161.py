class BigThing(object):
    def __init__(self, variable):
        self.__var = variable

    def size(self):
        # if type(self.__var) == int:
        if self.__var.isdigit():
            return self.__var
        else:
            return len(self.__var)


class BigCat(BigThing):
    def __init__(self, variable, weight):
        BigThing.__init__(self, variable)
        self.__weight = weight

    def size(self):
        if self.__weight > 20:
            return 'Very fat'
        elif self.__weight > 15:
            return 'Fat'
        else:
            'OK'


def main():
    my_thing = BigThing('table')
    print my_thing.size()

    latif = BigCat('latif', 22)
    print latif.size()


if __name__ == '__main__':
    main()
