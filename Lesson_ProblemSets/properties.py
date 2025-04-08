'''
1. create a Person class with a name setter and getter
'''

'''
2 disallow empty strings
'''

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Empty strings not allowed.')
        self._name = name

# adam = Person('Adam')
# print(adam.name) # Adam
# adam.name = 'Jeff'
# print(adam.name) # Jeff

# adam.name = ''

'''
Create a Rectangle class with attributes width and height. add properties to get width and height
but disallow modification after the object is created (no setters)
'''

class Rectangle:
    def __init__(self, height, width):
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._width
    
# arec = Rectangle(4, 5)
# print(arec.height)
# print(arec.width)
# arec.height = 7

'''
add a brightness property to the following class
'''
class SmartLamp:
    def __init__(self, color, brightness):
        self.color = color
        self.brightness = brightness

    def glow(self):
        return (f'The lamp glows {self.color} with brightness {self.brightness}%.')

    @property
    def color(self):                    # Getter for _color
        return self._color

    @color.setter
    def color(self, color):             # Setter for _color
        if not isinstance(color, str):
            raise TypeError('Color must be a color name.')

        self._color = color

    @property
    def brightness(self):
        return self._brightness
    
    @brightness.setter
    def brightness(self, brightness):
        if not isinstance(brightness, int):
            raise TypeError('Brightness must be an integer value between 0 and 100.')
        if brightness not in range(0, 101):
            raise ValueError('Brightness must be between 0 and 100.')
        self._brightness = brightness

# test cases: 
lamp = SmartLamp('blue', 70)
print(lamp.color)      # blue
print(lamp.brightness) # 70
print(lamp.glow())     # The lamp glows blue with brightness 70%.

lamp.color = 'red'
lamp.brightness = 90
print(lamp.color)      # red
print(lamp.brightness) # 90
print(lamp.glow())     # The lamp glows red with brightness 90%.

lamp.brightness = 120
# ValueError: Brightness must be between 0 and 100.