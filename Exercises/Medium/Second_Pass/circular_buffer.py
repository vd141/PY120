class CircularBuffer:
    '''
    an initialized buffer is an empty list

    check buffer length before get or put. if buffer length is 0, get returns None
    if buffer length is at full capacity, the oldest element is popped before putting a new element in


    '''

    def __init__(self, full_length):
        self._full_length = full_length
        self._buffer = []

    def get(self):
        if len(self._buffer) == 0:
            return None
        return self._buffer.pop(0)

    def put(self, value):
        if len(self._buffer) == self._full_length:
            self._buffer.pop(0)
        self._buffer.append(value)


buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
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