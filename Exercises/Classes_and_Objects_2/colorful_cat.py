'''
create a class named Cat that prints a greeting when the greet instance method
is invoked. The greeting should include the name and color of the cat. use a
class constant to define the color
'''

class Cat:
    _COLOR = 'pink'

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def greeting(self):
        print(f'Hello! My name is {self.name} and I\'m a {Cat._COLOR} cat!')

sophie = Cat('Sophie')

sophie.greeting()