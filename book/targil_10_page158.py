class Person(object):
    def __init__(self, name='Tal', age=20):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def __str__(self):
        return 'Person {} is {} years old'.format(self.__name, self.__age)


class Student(Person):
    def __init__(self, name='Alon', age=20, avg=80):
        Person.__init__(self, name, age)
        self.__avg = avg

    def set_avg(self, avg):
        self.__avg = avg

    def get_avg(self):
        return self.__avg

    def __str__(self):
        return 'Student {} is {} years old and his average: {}'.format(Person.get_name(self), Person.get_age(self),
                                                                       self.__avg)


def main():
    student1 = Student('Guy', 27, 100)
    student2 = Student()
    print student1
    print  student2


if __name__ == '__main__':
    main()
