#  init file
'''
defines a class and creates two objects from that class

class should have at least one instance variable that gets initialized by the
initializer

create a class for a running shoe
    - instance variable will be the color
'''

class RunningShoe:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        type_name = type(self).__name__
        print(f'I am a {self.brand} {self.model} {type_name} in {self.color}.')

RunningShoe('Saucony', 'Triumph', 'Blue')

'''
in 2 different ways, print the name of a class Foo without hardcoding it 
'''

class Foo:
    def __init__(self):
        print(type(self).__name__)
        print(self.__class__.__name__)

Foo()