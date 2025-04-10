'''
Q1

all are objects. class can be found by using type()
'''

'''
Q10: _cats_count is a class variable that tracks the number of intances
of the class. every time an instance is made, the variable is incremented
by one
'''

class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count

jack = Cat('tabby')
maisy = Cat('tabby')
charles = Cat('tabby')

print(Cat.cats_count()) #3