'''
create a class named Cat that prints a greeting when the greet instance method
is invoked. The greeting should include the name and color of the cat. use a
class constant to define the color
'''

class Cat:
    COLOR = 'blue'
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def greet(self):
        print(f'Hello! My name is {self.name} and I\'m a {Cat.COLOR} cat!')

kitty = Cat('Sophie')
kitty.greet()

# example output: Hello! My name is Sophie and I'm a purple cat!