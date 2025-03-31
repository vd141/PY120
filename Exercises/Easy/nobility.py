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

class Noble(WalkMixIn):
    '''
    nobility should be able to display name and title in walk function

    nobility name function should only return the name

    walk function in mixin currently uses name to display full name

    nobility can append the title to the name in walkmixin
    '''
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def walk(self):
        return f'{self.title} {super().walk()}'
    
    def gait(self):
        return 'struts'

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"