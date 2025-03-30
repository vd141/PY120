'''
create a class named Cat for which calling Cat.generic_greeting prints "Hello,
I'm a cat!"
'''

class Cat:

    @classmethod
    def generic_greeting(cls):
        print('Hello! I\'m a cat!')

    def not_a_class_method(): # (cls/self) throws an error if calling from class
        print(f'Hello. I am not a class method.')

kitty = Cat()

type(kitty).generic_greeting()

# type(kitty).not_a_class_method() 
''' 
can actually be called as a class method if there are no parameters. behaves like
a static method
'''

print(type(kitty) == Cat)