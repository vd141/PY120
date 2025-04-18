'''
name the method used to customize each of the following operators

> - __gt__
* - __mul__
<= - __le__
!= - __ne__
+= - __iadd__
**= - __ipow__
// - __floordiv__
'''

'''
create methods needed to compare cat objects for equality and inequality by
their name value. comparisons should ignore case and work for the == and != 
operators. if the right hand operand is not a Cat object, the methods should
return NotImplemented
'''

'''
create methods needed so you can perform ordered comparisons of Cat objects by their name value. 
comparisons should ignore case

add implementations for:
<
<=
>
>=
'''

class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() == other.name.casefold()

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.casefold() != other.name.casefold()

    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() < other.name.casefold()

    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() <= other.name.casefold()
    
    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() > other.name.casefold()
    
    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() >= other.name.casefold()


# jack = Cat('Jack')
# mandy = Cat('Mandy')
# jack2 = Cat('Jack')

# # print(jack == mandy)
# # print(jack != mandy)
# # print(jack == jack2)

# print(jack < mandy)
# print(jack <= mandy)
# print(mandy >= jack)
# print(mandy > jack)
# print(jack > mandy)
# print(jack >= mandy)
# print(mandy < jack)
# print(mandy <= jack)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        
        return Vector(self.x * other, self.y * other)
    
    def __rmul__(self, other):
        if not isinstance(other, int):
        if not isinstance(other, int):
            return NotImplemented
        
        return Vector(self.x * other, self.y * other)
        return Vector(self.x * other, self.y * other)


# print(Vector(3, 2) + Vector(5, 12))   # Vector(8, 14)
# print(Vector(5, 12) - Vector(3, 2))   # Vector(2, 10)
# print(Vector(5, 12) * 2)              # Vector(10, 24)
# print(3 * Vector(5, 12))              # Vector(15, 36)
# print(Vector(3, 2) + Vector(5, 12))   # Vector(8, 14)
# print(Vector(5, 12) - Vector(3, 2))   # Vector(2, 10)
# print(Vector(5, 12) * 2)              # Vector(10, 24)
# print(3 * Vector(5, 12))              # Vector(15, 36)

# my_vector = Vector(5, 7)
# my_vector += Vector(3, 9)
# print(my_vector)                      # Vector(8, 16)
# my_vector = Vector(5, 7)
# my_vector += Vector(3, 9)
# print(my_vector)                      # Vector(8, 16)

# my_vector -= Vector(1, 7)
# print(my_vector)                      # Vector(7, 9)
# my_vector -= Vector(1, 7)
# print(my_vector)                      # Vector(7, 9)

# print(Vector(3, 2) + 5)
# # TypeError: unsupported operand type(s) for +: 'Vector'
# # and 'int'

class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'

    def __add__(self, other):
        '''
        assuming Silly(x) + y

        if either x or y is a non-numeric string, concatenate the string values of x and y
        otherwise, compute the sum of the integer values of x and y
        '''

        if not isinstance(other, int):
            if not isinstance(other, str):
                return NotImplemented
            
        try:
            other_int = int(other)
            self_int = int(self.value)

            return Silly(other_int + self_int)
        except:
            return Silly(str(other) + str(self.value))


print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)