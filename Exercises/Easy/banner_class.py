'''
complete the following class so that the test cases work as intended
'''

class Banner:
    def __init__(self, message, length=None):
        # store message in private instance variable
        # store message length in private instance variable
        # width parameter specifies the desired length of the message
        # if the width is longer than the message, center the message
        self.message = message
        self.message_length = length
        if self.message_length == None or length < len(message):
            self.message_length = len(message)

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])
    
    @property
    def message(self):
        return self._message
    
    @message.setter
    def message(self, message):
        self._message = message
    
    @property
    def message_length(self):
        return self._message_length
    
    @message_length.setter
    def message_length(self, length):
        self._message_length = length

    def _empty_line(self):
        return f'| {self.message_length * ' '} |'

    def _horizontal_rule(self):
        return f'+-{self.message_length * '-'}-+'

    def _message_line(self):
        # build a list of strings where each string is a substring of the original
        # message and has a length of self.message_length
        return f"| {self.message.center(self.message_length)} |"
    

# Comments show expected output

banner = Banner('To boldly go where no one has gone before.', 1)
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