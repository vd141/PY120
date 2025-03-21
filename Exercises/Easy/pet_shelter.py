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
shelter keeps track of owner name and number of adoptions in a dict
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
        return self._name
    
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

    def number_of_pets(self):
        return len(self.pets)

class Shelter:
    def __init__(self):
        self._record = {}
        self._available = []

    def adopt(self, owner, pet):
        self._record[owner] = self._record.get(owner, 0) + 1
        owner.pets = pet

    def print_adoptions(self):
        for owner in self._record:
            print(f'{owner.name} has adopted the following pets:')
            for pet in owner.pets:
                print(f'a {pet.type} named {pet.name}.')

    def take_in(self, pet):
        self._available.append(pet)
        print(f'The shelter has taken in {pet.name}, a {pet.type}.')

    def display_available(self):
        print('The Animal Shelter has the following unadopted pets:')

        for pet in self._available:
            print(f'a {pet.type} named {pet.name}')

    def print_current_capacity(self):
        print(f'The Animal shelter has {len(self._available)} unadopted pets.')

    

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')
jack    = Pet('cat', 'Jack')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')
vdinh = Owner('V Dinh')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)
shelter.adopt(vdinh, jack)

print(phanson.number_of_pets())
print(bholmes.number_of_pets())

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")
print(f"{vdinh.name} has {vdinh.number_of_pets()} "
      "adopted pets.")

'''
adding unadopted pets to the animal shelter. store pets in a list.
loop through list to display animals


'''

asta = Pet('dog', 'Asta')
laddie = Pet('dog', 'Laddie')
fluffy = Pet('cat', 'Fluffy')
kat = Pet('cat', 'Kat')
ben = Pet('cat', 'Ben')
chatterbox = Pet('parakeet', 'Chatterbox')
bluebell = Pet('parakeet', 'Bluebell')

shelter.take_in(asta)
shelter.take_in(laddie)
shelter.take_in(fluffy)
shelter.take_in(kat)
shelter.take_in(ben)
shelter.take_in(chatterbox)
shelter.take_in(bluebell)

shelter.display_available()
shelter.print_current_capacity()