class CircularBuffer:
    '''
    init method takes a number that determines the length of the buffer

    buffer will store values in an array

    keep track of oldest and second oldest indexes with variables

    initialized array is full of Nones


    '''
    def __init__(self, buffer_length):
        self._buffer = [None for position in range(buffer_length)]
        self._length = buffer_length
        self._oldest_index = buffer_length

    def __str__(self):
        return str(self._buffer)

    def put(self, new_value):
        '''
        append the value to the buffer, pop the value from the front

        update oldest index
            oldest index starts at = length(buffer)
            if oldest index is greater than 0, decrement by 1
            if oldest index is 0, keep at 0
        '''

        self._buffer.append(new_value)
        self._buffer.pop(0)
        if self._oldest_index > 0:
            self._oldest_index -= 1


    def get(self):
        '''
        insert a None

        return the result of pop(0)
        '''

        self._buffer.append(None)
        if self._buffer.count(None) > 1:
            if all(item == None for item in self._buffer):
            return self._buffer.pop(self._oldest_index)
        return self._buffer.pop(0)
        

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

# buffer.put(3)
# buffer.put(4)
# print(buffer.get() == 2)             # True

# buffer.put(5)
# buffer.put(6)
# buffer.put(7)
# print(buffer.get() == 5)             # True
# print(buffer.get() == 6)             # True
# print(buffer.get() == 7)             # True
# print(buffer.get() is None)          # True

# buffer2 = CircularBuffer(4)

# print(buffer2.get() is None)         # True

# buffer2.put(1)
# buffer2.put(2)
# print(buffer2.get() == 1)            # True

# buffer2.put(3)
# buffer2.put(4)
# print(buffer2.get() == 2)            # True

# buffer2.put(5)
# buffer2.put(6)
# buffer2.put(7)
# print(buffer2.get() == 4)            # True
# print(buffer2.get() == 5)            # True
# print(buffer2.get() == 6)            # True
# print(buffer2.get() == 7)            # True
# print(buffer2.get() is None)         # True