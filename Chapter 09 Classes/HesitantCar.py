 from Car_8 import Car
 
 class HesitantRobot(Car):
     def __init__(self, name = None, times = 1):
         super().__init__(name = name)
         self.__times = times
 
     def say_hi(self):
         print('"', 'um ...' * self.__times, 'hi!", said', super().name)
 
     def say_goodbye(self):
         print('"', 'um ...' * self.__times, 'goodbye!", said', super().name)