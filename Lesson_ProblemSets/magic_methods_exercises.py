class Car:
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        self.__color = color.title()

    def __str__(self):
        return f'{self.__color} {self.__year} {self.__model}'
    
    def __repr__(self):
        return f'Car({repr(self.__model)}, {self.__year}, {repr(self.__color)})'
    

vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')