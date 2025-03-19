class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_wheels(self):
        return self.wheels
    
    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
        self.wheels = 4

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
        self.wheels = 2


class Truck(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
        self.wheels = 6

toyota = Car('toyota', 'venza')
print(toyota.make, toyota.model, toyota.get_wheels())

triumph = Motorcycle('triumph', 'detroit')
print(triumph.make, triumph.model, triumph.get_wheels())

f150 = Truck('ford', 'f150')
print(f150.make, f150.model, f150.get_wheels())


'''
refactor the classes so they use a common superclass

all have a make/model attribute

get_wheels is common, but returns different values. these can be initiated 
in init for each vehicle

info is the same for each

create a vehicle class
'''

