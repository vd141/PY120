'''
write the classes and methods necessary for the code to run and produce the
following output:

P Hanson has adopted the following pets:
a cat named Cocoa
a cat named Cheddar
a bearded dragon named Darwin

B Holmes has adopted the following pets:
a dog named Molly
a parakeet named Sweetie Pie
a dog named Kennedy
a fish named Chester

P Hanson has 3 adopted pets.
B Holmes has 4 adopted pets.
'''

'''
pet class will have a type and name attributes

owner class will have name, iist of adopted pets, and pet count attributes

shelter adopt method adds pet to owner's list
shelter print adoptions method accesses owner class's name and list 
'''

class Pet:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        self._type = type

    @property
    def name(self):
        return self.__qualname__
    
    @name.setter
    def name(self, name):
        self._name = name

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []
        self.pet_count = len(self.pets)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def pets(self):
        return self._pets
    
    @pets.setter
    def pets(self, pet):
        self._pets.append(pet)

    @property
    def pet_count(self):
        return self._pet_count

    @pet_count.setter
    def pet_count(self, count):
        self._pet_count = count



cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

# phanson = Owner('P Hanson')
# bholmes = Owner('B Holmes')

# shelter = Shelter()
# shelter.adopt(phanson, cocoa)
# shelter.adopt(phanson, cheddar)
# shelter.adopt(phanson, darwin)
# shelter.adopt(bholmes, kennedy)
# shelter.adopt(bholmes, sweetie)
# shelter.adopt(bholmes, molly)
# shelter.adopt(bholmes, chester)

# shelter.print_adoptions()
# print(f"{phanson.name} has {phanson.number_of_pets()} "
#       "adopted pets.")
# print(f"{bholmes.name} has {bholmes.number_of_pets()} "
#       "adopted pets.")