'''
write a class such that the following code prints the results indicated by
the comments
'''

class Transform:
    def __init__(self, input_string):
        self._string = input_string

    def uppercase(self):
        return self._string.upper()
    
    @classmethod
    def lowercase(cls, input_str):
        return input_str.lower()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz

