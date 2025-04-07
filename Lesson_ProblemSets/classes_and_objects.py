class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    @property
    def name(self):
        return f'{self._firstname} {self._lastname}'.strip()

    @name.setter
    def name(self, name):
        # edge cases
        # empty names
        # only first name
        # two names
        names = name.split()

        match len(names):
            case 0:
                self.first_name = ''
                self.last_name = ''
            case 1:
                self.first_name = names[0]
                self.last_name = ''
            case _:
                self.first_name = names[0]
                self.last_name = ' '.join(names[1:])

    @property
    def first_name(self):
        return self._firstname
    
    @first_name.setter
    def first_name(self, name):
        self._firstname = name
    
    @property
    def last_name(self):
        return self._lastname

    @last_name.setter
    def last_name(self, name):
        self._lastname = name

    
# problem 1
# bob = Person('bob')
# print(bob.name)           # bob
# bob.name = 'Robert'
# print(bob.name)           # Robert

# problem 2
# bob = Person('Robert')
# print(bob.name)             # Robert
# print(bob.first_name)       # Robert
# print(repr(bob.last_name))  # ''
# bob.last_name = 'Smith'
# print(bob.name)             # Robert Smith

# problem 3
# bob = Person('Robert')
# print(bob.name)             # Robert
# print(bob.first_name)       # Robert
# print(repr(bob.last_name))  # ''
# bob.last_name = 'Smith'
# print(bob.name)             # Robert Smith

# bob.name = 'Prince'
# print(bob.first_name)       # Prince
# print(repr(bob.last_name))  # ''

# bob.name = 'John Adams'
# print(bob.first_name)       # John
# print(bob.last_name)        # Adams

# problem 4
# bob = Person('Robert Smith')
# rob = Person('Robert Smith')

# print(bob.name == rob.name)

# problem 5
bob = Person('Robert Smith')
print(f"The person's name is: {bob}")