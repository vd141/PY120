'''
modify Truck.start_engine by appending "Drive fast, please!" to the return value
of Vehicle.start_engine. The 'fast' in "Drive fast, please!" should be taken from
the value of the speed argument
'''

class Vehicle:
    def start_engine(self):
        return 'Ready to go!'

class Truck(Vehicle):
    def start_engine(self, speed):
        self.speed = speed
        return super().start_engine() + f' Drive {self.speed}, please!'
    
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, speed):
        self._speed = speed

# Comments show expected output
truck1 = Truck()
print(truck1.start_engine('fast'))
# Ready to go! Drive fast, please!

truck2 = Truck()
print(truck1.start_engine('slow'))
# Ready to go! Drive slow, please!