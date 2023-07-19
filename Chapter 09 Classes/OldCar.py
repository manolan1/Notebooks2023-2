from HesitantCar import HesitantCar

class OldCar(HesitantCar):
    def __init__(self, name = None, times = 3, age = 0):
        super().__init__(name = name, times = times)
        self.__set_age(age)

    def __set_age(self, age):
        if age < 70:
            self.__age = 70
        else:
            self.__age = age

    def __get_age(self):
        return self.__age

    age = property(__get_age, __set_age)
