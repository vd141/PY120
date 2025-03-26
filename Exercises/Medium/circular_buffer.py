class CircularBuffer:
    '''
    init method takes a number that determines the length of the buffer

    buffer will store values in an array

    initialized array is empty

    oldest value in buffer is always the element at index 0
    '''
    def __init__(self, buffer_length):
        self._buffer = []
        self._max_length = buffer_length
        self._oldest_index = 0

    def __str__(self):
        return str(self._buffer)

    def put(self, new_value):
        '''
        append the value to the buffer, 
        
        pop the value from the front if buffer length is currently at initialized length

        '''

        self._buffer.append(new_value)
        if len(self._buffer) > self._max_length:
            self._buffer.pop(self._oldest_index)



    def get(self):
        '''
        if buffer is empty, return None

        otherwise, pop the element at the beginning of the buffer
        '''

        if len(self._buffer) == 0:
            return None
        return self._buffer.pop(self._oldest_index)
        

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True


buffer.put(1)
buffer.put(2)
print(buffer)
print(buffer.get() == 1)             # True
print(buffer)

buffer.put(3)
buffer.put(4)
print(buffer)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True