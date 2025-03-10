'''
p1

add a parameter to __init__ that provides a name for the Cat object. use an instance
variable to print a greeting with the provided name
'''

# class Cat:
#     def __init__(self, name):
#         self._name = name
#         print(f'My name is {self._name}.')

# kitty = Cat('Tammy')

'''
p2

move the greeting from __init__ to a method named greet() that prints the greeting
when invoked
'''

class Cat:
    def __init__(self, name):
        self._name = name

    def greet(self):
        print(f'My name is {self._name}.')

kitty = Cat('Tammy')
kitty.greet()