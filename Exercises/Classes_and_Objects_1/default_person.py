'''
create a class named Person

when the class is created, it should be instantiated with in input name

if no name is given, the default name should be john doe
'''

class Person:
    def __init__(self, name='John Doe'):
        self._name = name

    @property
    def name(self):
        return self._name
    
person1 = Person()
person2 = Person('Pepe le Pew')

print(person1.name)
print(person2.name)
