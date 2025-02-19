import math

# class Car:
#     def __init__(self, model, year, color):
#         self._model = model
#         self._year = year
#         self._color = color

#     def __repr__(self):
#         return f'{self.__class__.__name__}({repr(self._model)}, {repr(self._year)}, {repr(self._color)})'
    
#     def __str__(self):
#         return f'{self._color.title()} {self._year} {self._model.title()}'

# vwbuzz = Car('ID.Buzz', 2024, 'red')
# print(vwbuzz)        # Red 2024 ID.Buzz
# print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        x = self.x - other.x
        y = self.y - other.y

        return Vector(x, y)
    
    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        return self.x * other.x + self.y * other.y


    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

        
    # __iadd__ method omitted; we don't need it for this exercise

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'

v1 = Vector(5, 12)
v2 = Vector(13, -4)
print(v1 + v2)      # Vector(18, 8)

print(v1 - v2) # Vector(-8, 16)
print(v1 * v2) # 17
print(abs(v1)) # 13.0