class Car:
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self._speed = 0

    @classmethod
    def mileage(cls, miles, gallons):
        mpg = miles / gallons
        print(f'Miles per gallon is {mpg:.2f}.')

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_speed):
        self._speed = new_speed
        return self._speed
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year

    def engine_on(self):
        if self._speed == 0:
            print('Engine is on! Speed is 0.')
        else:
            print(f'Engine is already running and speed is {self._speed}')
        pass

    def accelerate(self, new_speed):
        self._speed = new_speed
        print(f'Accelerating. Speed increased to {new_speed}')

    def brake(self, new_speed):
        self._speed = new_speed
        print(f'Braking. Speed reduced to {new_speed}')

    def engine_off(self):
        if self.speed == 0:
            print('Engine is now off. Speed is 0.')
        else:
            print('Brake to a stop before turning engine off!')
        self._speed = 0

    def spray_paint(self, new_color):
        self._spray_paint_color = new_color
        self._color = self._spray_paint_color

toyota = Car('prius', '2025', 'white')

# toyota.engine_on()
# toyota.accelerate(40)
# toyota.brake(20)
# toyota.brake(0)
# toyota.engine_off()

print(toyota.color)
toyota.color = 'pink'
print(toyota.color)
print(toyota.model)
print(toyota.year)
toyota.spray_paint('yellow')
print(toyota.color)
# toyota.model = 'camry'
# toyota.year = 2024

Car.mileage(47, 2.5)

# class Person:
#     def __init__(self, first, last):
#         if self._validate(first):
#             self._first = first
#         if self._validate(last):
#             self._last = last

#     @property
#     def name(self):
#         return ' '.join([self._first.title(), self._last.title()])
    
#     @name.setter
#     def name(self, new_name):
#         if not isinstance(new_name, tuple):
#             raise TypeError('Input must be a tuple.')
#             return False
#         if self._validate(new_name[0]) and self._validate(new_name[1]):
#             self._first, self._last = new_name
    
#     @staticmethod
#     def _validate(name):
#         if name == '':
#             raise ValueError('All characters must be alphabetic')
#             return False
#         for char in name:
#             if not char.isalpha():
#                 raise ValueError('All characters must be alphabetic')
#                 return False
        
#         return True
    
# actor = Person('Mark', 'Sinclair')
# print(actor.name)              # Mark Sinclair
# actor.name = ('Vin', 'Diesel')
# print(actor.name)              # Vin Diesel
# actor.name = ('', 'Diesel')
# # ValueError: Name must be alphabetic.

# character = Person('annIE', 'HAll')
# print(character.name)          # Annie Hall
# character = Person('Da5id', 'Meier')
# # ValueError: Name must be alphabetic.

friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.