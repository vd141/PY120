'''
using the code snippet below, add a getter method named name and invoke it in
place of self._name in greet
'''

class Cat:
    def __init__(self, name):
        self._name = name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

    @property
    def name(self):
        return self._name

kitty = Cat('Sophie')
kitty.greet()