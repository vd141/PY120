# update the code so that instead of printing the value, Python prints the name
# of the class to which it belongs

# create a new class for each that inherits the original class and overrides the
# __str__ method (because print implicitly uses __str__)

# str cannot be subclassed directly for mutable behavior

class Wagyu:
    def __init__(self):
        pass

bake = Wagyu()

print(bake)

# Comments show expected output
print("Hello")                # <class 'str'>
print(5)                      # <class 'int'>
print([1, 2, 3])              # <class 'list'>

print(type('Hello'))
print(type(5))
print(type([1, 2, 3]))