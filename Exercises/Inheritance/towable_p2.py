'''
create a class named Vehicle that, upon instantiation, assigns the passed in 
argument to self.year. Both Truck and Car should inherit from Vehicle
'''

class Vehicle:
    def __init__(self, year):
        self.year = year

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year):
        self._year = year

class TowingMixin:
    def tow(self):
        return 'I can tow a trailer!'

class Truck(TowingMixin, Vehicle):
    pass

class Car(Vehicle):
    pass

# Comments show expected output
truck1 = Truck(1994)
print(truck1.year)            # 1994
print(truck1.tow())           # I can tow a trailer!

car1 = Car(2006)
print(car1.year)              # 2006