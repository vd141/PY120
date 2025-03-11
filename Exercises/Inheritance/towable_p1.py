'''
create a Towable mixin that contains a method tow. this method should print
"I can tow a trailer!" when invoked. The mixin should be included in the Truck class
'''

class Towable:
    def tow(self):
        print('I can tow a trailer!')

class Truck(Towable):
    pass

class Car:
    pass

# Comments show expected output
truck1 = Truck()
truck1.tow()        # I can tow a trailer!

car1 = Car()
car1.tow()
# AttributeError: 'Car' object has no attribute 'tow'