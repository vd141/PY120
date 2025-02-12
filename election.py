class Candidate:
    '''
    candidates takes a full name string and creates a candidate object
        - create a setter method to validate that full_name was saved
        - create str method to output the name stored in that instance
        - create repr method to output the repr of that instance

    a candidate object can use the in-place augmented assignment addition operator
    to add to the count of existing Candidate objects
        - create a class variable to keep track of total class instances
        - create a class method to return class instance total
        - create a class dict to track occurences of each unique class instance
            - check dictionary to see if that instance exists in teh dict. if not, add instance to dict
              and increase count to 1. if exists, then increase count by 1
        - create class method to show instances dict

    it can also use the in-place augmented assignment addition operator to add to the count
    of equal candidate objects
    '''

    counter = 0

    instances = {}

    
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
    
    @classmethod
    def instance_count(cls):
        return cls.counter

    def __iadd__(self, addend):
        Candidate.counter += addend
        Candidate.instances[self.name] = Candidate.instances.get(self.name, 0) + 1

    @classmethod
    def show_all_votes(cls):
        return Candidate.instances

    def show_candidate_votes(self):
        return Candidate.instances[self.name]

class Election:
    '''
    the Election class takes a set of unique candidates
        

    the Election class prints the election results using the results method
        - loop through the unique candidates
            - gets the candidate name
        - find the candidate key:value pair in the candidate class
        - add to an f string
        - store f string in list of f strings
        - add the winning candidate's percentage of total votes
            - determine the candidate with most votes.
            - divide that number by the total number of votes

    the results method can 
        - display each unique candidate's name
        - count the number of votes each candidate has
        - display the percentage of votes the winner had
    '''

    candidate_results = []
    
    def __init__(self, candidates):
        for candidate in candidates:
            self.candidate_results.append(f'{candidate.name}: {candidate.show_candidate_votes()} votes')

        self.candidate_results.append('')
        winner_percentage = candidate.show_all_votes()[max(candidate.show_all_votes())] / candidate.__class__.instance_count() * 100
        self.candidate_results.append(f'{max(candidate.show_all_votes())} won: {winner_percentage:.1f}% of votes')

    def results(self):
        for line in self.candidate_results:
            print(line)

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1


election = Election(candidates)
election.results()