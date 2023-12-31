class Car:
    """
       This is the eighth class, also base class
    """

    __count = 0

    def __init__(self, name = None):
        self.__set_name(name)
        type(self).__count += 1

    def __del__(self):
        type(self).__count -= 1

    def say_hi(self):
        print(self.name, ', says "hi!"')

    def __set_name(self, name):
        if name:
            self.__name = name
        else:
            self.__name = "Unknown"

    def __get_name(self):
        return self.__name

    @staticmethod
    def car_count():
        return Car.__count

    @classmethod
    def class_count(cls):
        return cls.__count

    def __str__(self):        
        return 'Car with name ' + self.__get_name()

    def __gt__(self, other):
        return self.name > other.name

    name = property(__get_name, __set_name)
