# if i define a class method, can it be used in an instance of the class?
# it can be

class Vehicle:
    def __init__(self, year, color):
        self.__year = year
        self.__color = color

    @classmethod
    def year(cls):
        print('hello')
        return 'hello'
    
    # @property
    # def year(self):
    #     return self.__year
    
a_car = Vehicle(1994, 'blue')
print(a_car.year())