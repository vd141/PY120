'''
create a new class called Cat that can do everything a dog can except fetch
'''

class Quadripet:
    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Dog:
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'
    
class Cat(Quadripet):
    def speak(self):
        return 'meow!'
    
    def scratch(self):
        return 'meowrrrrrr'

tammy = Cat()
print(tammy.scratch())