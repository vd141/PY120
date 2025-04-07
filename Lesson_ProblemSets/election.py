class Candidate:
    '''
    the Candidate constructor takes a string of the candidate's full name

    a candidate object can perform in place addition
    '''

    __candidate_count = 0

    def __init__(self, full_name):
        self.__full_name = full_name

    def __iadd__(cls, other):
        if not isinstance(other, int):
            return NotImplemented
        
        cls.__candidate_count += other
        
    @property
    def candidate_count(cls):
        return cls.__candidate_count


class Election:
    def __init__(self):
        pass




mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

print(Candidate.candidate_count)

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