'''
1.
'''

'''
2
add get_breed to the Dog class 
'''

class Dog:
    def __init__(self, breed=None):
        self._breed = breed

    def get_breed(self):
        return self._breed

# # Test cases
# dog1 = Dog('Golden Retriever')
# dog2 = Dog('Poodle')
# print(dog1.breed) # Golden Retriever
# print(dog2.breed) # Poodle
# print(dog1.get_breed())
# print(dog2.get_breed())

'''
3
create a Cat class that has a single method get_name
'''

class Cat:
    def __init__(self):
        pass

    def get_name(self):
        try:
            return self.name
        except AttributeError:
            print('Name not set!')

# cat1 = Cat()
# cat1.get_name()

'''
4
'''
# dog3 = Dog()
# dog3._breed = 'Wilbur'
# print(dog3._breed)

'''
5
'''
class Student:
    school_name = 'Oxford'

    def __init__(self, name=None):
        self.name = name

    @classmethod
    def school_name_method(cls):
        return Student.school_name
    

# stu1 = Student()
# print(stu1.__class__.school_name)

'''
6
'''

stu1 = Student('Jamie')
stu2 = Student('Olaf')

# print(stu1.name)
# print(stu2.name)
# print(stu1.__class__.school_name)
# print(stu2.__class__.school_name)

'''
7
'''
# print(Student.school_name)
# print(Student.school_name_method())

'''
8
'''
class Car:
    manufacturer = 'Ford'
    def __init__(self):
        self.manufacturer = 'Toyota'

    def show_manufacturer(self):
        print(f'Class variable: {self.__class__.manufacturer=}')
        print(f'Instance variable: {self.manufacturer=}')

# car1 = Car()
# car1.show_manufacturer()

'''
9
'''
class Bird:
    species = 'sparrow'
    def __init__(self, species=None):
        pass

class Sparrow(Bird):
    pass

# print(Sparrow().species)

'''
10
'''
class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        self.color = color

birdie = Sparrow("sparrow", "brown")
# print(birdie.species)               # What will this output?
# this will throw an exception because species has not been assigned to a value. the __init__ method in 
# Sparrow shadows the __init__ method in Bird, so self.species is not assigned to species

'''
11
'''
class Mammal:
    def __init__(self):
        self.legs = 4

class Human(Mammal):
    def __init__(self):
        super().__init__()
        self.legs = 2

# hum1 = Human()
# print(hum1.legs)

'''
12
'''
class Cat:
    sound = "meow"

    @classmethod
    def make_sound(cls):
        return cls.sound

class Lion(Cat):
    sound = "roar"

print(Lion.make_sound()) # What will this output?
# it will print roar because the cls variable sound has been set to roar in Lion

'''
13
'''
class Tree:
    def __init__(self):
        self.type = "Generic Tree"

class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"

# Pine's type attribute will be Pine Tree because its __init__ method reassigns the type variable that was
# assigned in the super's __init__ method

'''
14
'''
class A:
  def __init__(self):
      self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)

# this code would throw an exception because B's __init__ method shadow's A's __init__ method
# var_a is not assigned in B's __init__ method
# exception type: AttributeError

