'''
create a subclass from Dog called Bulldog that overrides the sleep method to
return "snoring"
'''

class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'
    
class Bulldog(Dog):
    def sleep(self):
        return 'snoring!'

teddy = Dog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!

maruchan = Bulldog()
print(maruchan.speak()) # bark1
print(maruchan.sleep()) # snoring