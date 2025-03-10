'''
create a class named Cat for which calling Cat.generic_greeting prints "Hello,
I'm a cat!"
'''

class Cat:

    @classmethod
    def generic_greeting(cls):
        print('Hello! I\'m a cat!')

kitty = Cat()

type(kitty).generic_greeting()

print(type(kitty) == Cat)