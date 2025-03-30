'''
create two classees, Truck and Car that inherity from Vehicle
'''

class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year
    
class Truck(Vehicle):
    def __init(self, year):
        super().__init__(year)

class Car(Vehicle):
    def __init(self, year):
        super().__init__(year)

# Comments show expected output
truck1 = Truck(1994)
print(truck1.year)            # 1994

car1 = Car(2006)
print(car1.year)              # 2006