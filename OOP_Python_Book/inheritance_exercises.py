class Vehicle:
    count = 0
    def __init__(self):
        Vehicle.count += 1

    @classmethod
    def vehicles(cls):
        return Vehicle.count
    
class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)

    @classmethod
    def vehicles(cls):
        return Vehicle.vehicles()

class Truck(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)

    @classmethod
    def vehicles(self):
        return Vehicle.vehicles()
    
class Boat(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)

    @classmethod
    def vehicles(self):
        return Vehicle.vehicles()


print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8