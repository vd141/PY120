'''
complete the following class so that the test cases work as intended
'''

class Banner:
    def __init__(self, message):
        # store message in private instance variable
        # store message length in private instance variable
        self._message = message
        self._message_length = len(message)

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])
    
    @property
    def message(self):
        return self._message
    
    @property
    def message_length(self):
        return self._message_length

    def _empty_line(self):
        return f'| {self.message_length * ' '} |'

    def _horizontal_rule(self):
        return f'+-{self.message_length * '-'}-+'

    def _message_line(self):
        return f"| {self.message} |"
    

# Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+