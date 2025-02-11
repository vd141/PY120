class Car:
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        self.__color = color

        self.__speed = 0

    @classmethod
    def mpg(cls, miles, gallons):
        return miles / gallons

    def engine_on(self):
        print(f'The {self.__color} {self.__year} {self.__model} is now on.')

    def accelerate(self, speed):
        print(f'The {self.__color} {self.__year} {self.__model} is now accelerating '
              f'by {speed} mph.')
        self.__speed += speed

    def brake(self, speed):
        print(f'The {self.__color} {self.__year} {self.__model} is now braking by '
              f'{speed} mph.')
        self.__speed -= speed

    def engine_off(self):
        self.speed = 0
        print(f'The {self.__color} {self.__year} {self.__model} is now off.')

    def current_speed(self):
        print(f'The {self.__color} {self.__year} {self.__model}\'s current speed is '
              f'{self.__speed}')
        
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def model(self):
        return self.__model
    
    @property
    def year(self):
        return self.__year
    
    def spray_color(self, color):
        print(f'The car is being sprayed {color}!')
        self.__color = color

    @staticmethod
    def driver_message(sentence):
        print(f'VROOM VROOM {sentence}')

# toyota = Car('Crosstrek', 2025, 'Gray')
# toyota.engine_on()
# toyota.accelerate(35)
# toyota.current_speed()
# toyota.brake(21)
# toyota.current_speed()
# toyota.brake(14)
# toyota.current_speed()
# toyota.engine_off()
# toyota.current_speed()
# print(toyota.color)
# toyota.color = 'astrid'
# print(toyota.color)
# print(toyota.model)
# print(toyota.year)
# toyota.spray_color('cerulean')
# print(Car.mpg(47, 1.2))


class Person:
    def __init__(self, first, last):
        self.__name_setter((first, last))

    @property
    def full_name(self):
        return self.__first.title() + ' ' + self.__last.title()
    
    @full_name.setter
    def full_name(self, full_name_tuple):
        self.__name_setter(full_name_tuple)

    @classmethod
    def __validate(cls, full_name_tuple):
        if '' in full_name_tuple:
            raise ValueError('All characters must be alphabetic.')
        if not isinstance(full_name_tuple, tuple):
            raise TypeError('Input must be a tuple.')
        for char in set(full_name_tuple[0] + full_name_tuple[1]):
            if not char.isalpha():
                raise ValueError('All characters must be alphabetic.')

    def __name_setter(self, full_name_tuple):
        Person.__validate(full_name_tuple)
        self.__first, self.__last = full_name_tuple


# actor = Person('Mark', 'Sinclair')
# print(actor.full_name)              # Mark Sinclair
# actor.full_name = ('Vin', 'Diesel')
# print(actor.full_name)              # Vin Diesel
# actor.full_name = ('', 'Diesel')
# # ValueError: Name must be alphabetic.

# character = Person('annIE', 'HAll')
# print(character.full_name)          # Annie Hall
# character = Person('Da5id', 'Meier')
# # ValueError: Name must be alphabetic.

# friend = Person('Lynn', 'Blake')
# print(friend.full_name)             # Lynn Blake
# friend.full_name = ('Lynn', 'Blake-John')
# # ValueError: Name must be alphabetic.

subaru = Car.driver_message('hihi hehe')