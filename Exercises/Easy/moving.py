class Person:
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

class Cat:
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah:
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"
    
'''
update class definitions to enable the following code


'''
mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"