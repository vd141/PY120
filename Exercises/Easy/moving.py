class WalkMixIn:
    def walk(self):
        return f'{self.name} {self.gait()} forward'

class Person(WalkMixIn):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

class Cat(WalkMixIn):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah(WalkMixIn):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"
    
'''
update class definitions to enable the following code

can use a Walker mixin that includes a walk() method. the walk method calls each
class's gait() method to create the output string
'''


mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"