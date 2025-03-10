# # every object instance adds 1 to the vehicle count.
# # Car, Truck, and Boat add to the parent class's vehicle count
# # parent class should be called vehicle. Car, Truck, and Boat inherit from Vehicle
# # the vehicle count is a Vehicle class variable that gets updated when a child is instantiated

# class Vehicle:
#     _vehicle_count = 0

#     def __init__(self):
#         Vehicle._vehicle_count += 1

#     @classmethod
#     def vehicles(cls):
#         return cls._vehicle_count
    
# class SignalMixIn:
#     def signal_left(self):
#         print('Signalling left')

#     def signal_right(self):
#         print('Signalling right')

#     def signal_off(self):
#         print('Signal is now off')

# class Car(Vehicle, SignalMixIn):
#     def __init__(self):
#         super().__init__()

# class Truck(Vehicle, SignalMixIn):
#     def __init__(self):
#         super().__init__()

# class Boat(Vehicle):
#     def __init__(self):
#         super().__init__()





# print(Car.vehicles())     # 0
# car1 = Car()
# print(Car.vehicles())     # 1
# car2 = Car()
# car3 = Car()
# car4 = Car()
# print(Car.vehicles())     # 4
# truck1 = Truck()
# truck2 = Truck()
# print(Truck.vehicles())   # 6
# boat1 = Boat()
# boat2 = Boat()
# print(Boat.vehicles())    # 8

# car1.signal_left()       # Signalling left
# truck1.signal_right()    # Signalling right
# car1.signal_off()        # Signal is now off
# truck1.signal_off()      # Signal is now off
# # boat1.signal_left()
# # AttributeError: 'Boat' object has no attribute
# # 'signal_left'

# print(Car.mro())
# print(Truck.mro())
# print(Boat.mro())
# print(Vehicle.mro())

class Vehicle:
    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg

    def max_range_in_miles(self):
        return self.capacity * self.mpg

class Car(Vehicle):
    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def family_drive(self):
        print('Taking the family for a drive')

class Truck(Vehicle):
    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def hookup_trailer(self):
        print('Hooking up trailer')

car = Car(12.5, 25.4)
truck = Truck(150.0, 6.25)

print(car.max_range_in_miles())         # 317.5
print(truck.max_range_in_miles())       # 937.5

car.family_drive()     # Taking the family for a drive
truck.hookup_trailer() # Hooking up trailer

try:
    truck.family_drive()
except AttributeError:
    print('No family_drive method for Truck')
# No family_drive method for Truck

try:
    car.hookup_trailer()
except AttributeError:
    print('No hookup_trailer method for Car')
# No hookup_trailer method for Car