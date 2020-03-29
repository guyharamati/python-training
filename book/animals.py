class Dog:
    def __init__(self, name='Quatro', age=1):
        self.__name = name
        self.__age = age

    def birthday(self):
        self.age += 1

    def set_name(self, name):
        self.__name = name

    def get_dog(self):
        return self.__name, self.__age

    def __str__(self):
        return 'Dog_name:{} , Dog_age:{} years old'.format(self.__name, self.__age)
