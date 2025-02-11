class Candidate:
    '''
    candidates takes a full name string and creates a candidate object
        - create a setter method to validate that full_name was saved
        - create str method to output the name stored in that instance
        - create repr method to output the repr of that instance

    a candidate object can use the in-place augmented assignment addition operator
    to add to the count of existing Candidate objects

    it can also use the in-place augmented assignment addition operator to add to the count
    of equal candidate objects
    '''
    
    def __init__(self, full_name):
        self.__name = full_name

    @property
    def name(self):
        return self.__full_name
    
    @name.setter
    def __name(self, full_name):
        self.__full_name = full_name

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'Candidate({repr(self.name)})'
    
mike_jones = Candidate('Mike Jones')
print(mike_jones)
print(repr(mike_jones))

class Election:
    '''
    the Election class takes a set of candidates

    the Election class prints the election results using the results method

    the results method can 
        - display each unique candidate's name
        - count the number of votes each candidate has
        - display the percentage of votes the winner had
    '''
    pass

# mike_jones = Candidate('Mike Jones')
# susan_dore = Candidate('Susan Dore')
# kim_waters = Candidate('Kim Waters')

# candidates = {
#     mike_jones,
#     susan_dore,
#     kim_waters,
# }

# votes = [
#     mike_jones,
#     susan_dore,
#     mike_jones,
#     susan_dore,
#     susan_dore,
#     kim_waters,
#     susan_dore,
#     mike_jones,
# ]

# for candidate in votes:
#     candidate += 1

# election = Election(candidates)
# election.results()