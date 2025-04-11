'''
1

Alyssa is correct because .balance is a property that accesses ._balance
'''
class BankAccount:
    def __init__(self, starting_balance):
        self._balance = starting_balance

    def balance_is_positive(self):
        return self.balance > 0

    @property
    def balance(self):
        return self._balance

'''
2

update InvoiceEntry so it functions as shown
'''
class InvoiceEntry:
    def __init__(self, product_name, number_purchased):
        self._product_name = product_name
        self._quantity = number_purchased

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, new_quant):
        self._quantity = new_quant

entry = InvoiceEntry('Marbles', 5000)
print(entry.quantity)         # 5000

entry.quantity = 10_000
print(entry.quantity)         # 10_000

'''
3
'''
class Animal:
    def speak(self, sounds):
        print(sounds)

class Cat(Animal):
    @classmethod
    def meow(cls):
        Animal().speak('Meow!')

class Dog(Animal):
    @classmethod
    def bark(cls):
        Animal().speak('Woof! Woof! Woof!')

Cat.meow()
Dog.bark()

'''
4
'''
class KrispyKreme:
    def __init__(self, filling, glazing):
        self.filling = filling
        self.glazing = glazing

    # def __str__(self):
    #     filling = self.filling
    #     glazing = self.glazing
    #     if not (filling or glazing):
    #         return 'Plain'
    #     if filling and not glazing:
    #         return filling
    #     if not filling and glazing:
    #         return f'Plain with {glazing}'
    #     if filling and glazing:
    #         return f'{filling} with {glazing}'
    def __str__(self):
        options = []
        options.append(self.filling or 'Plain')
        if self.glazing:
            options.append(self.glazing)

        return ' with '.join(options)

donut1 = KrispyKreme(None, None)
donut2 = KrispyKreme('Vanilla', None)
donut3 = KrispyKreme(None, 'sugar')
donut4 = KrispyKreme(None, 'chocolate sprinkles')
donut5 = KrispyKreme('Custard', 'icing')

print(donut1)       # Plain
print(donut2)       # Vanilla
print(donut3)       # Plain with sugar
print(donut4)       # Plain with chocolate sprinkles
print(donut5)       # Custard with icing

'''
5

change the light_status method name so that the name is clearer and less repetitive
'''
class Light:
    def __init__(self, brightness, color):
        self.brightness = brightness
        self.color = color

    def status(self):
        return (f'I have a brightness level of {self.brightness} '
                f'and a color of {self.color}')

my_light = Light(50, 'Red')
print(my_light.status())