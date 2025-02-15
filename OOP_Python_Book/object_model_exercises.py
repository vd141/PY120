'''
define a class and create two objects from that class

class should have at least one instance variable that gets initialized by the
initializer

'''

class Bird:
    def __init__(self):
        self._flies = True

    @property
    def flies(self):
        return self._flies
    
class Flamingo(Bird):
    def __init__(self):
        self._flies = False

turkey_vulture = Bird()
pigeon = Bird()

# print(turkey_vulture.flies)

flamingo = Flamingo()
print(flamingo.flies)

'''
given a Foo object, what are two different ways to print 'I am a Foo object'
without hardcoding Foo
'''

class Foo:
    def __init__(self):
        pass

a = Foo()
print(type(a).__name__)
print(a.__class__.__name__)