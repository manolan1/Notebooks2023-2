class Car:
    """
       This is the seventh class
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

    name = property(__get_name, __set_name)
