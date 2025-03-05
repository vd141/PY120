
class Candidate:
    def __init__(self, name):
        self._name = name
        self._count = 0

    def __iadd__(self, num):
        self._count += num

    @property
    def name(self):
        return self._name
    
    @property
    def count(self):
        return self._count
    
class Election:
    def __init__(self, candidates):
        self._total_votes = 0
        self._winner = None
        self._winner_votes = 0

        max = 0

        for candidate in candidates:
            Election._print_results(candidate)
            self._total_votes += candidate.count
            if candidate.count > max:
                max = candidate.count
                self._winner = candidate.name
                self._winner_votes = candidate.count

    @staticmethod
    def _print_results(candidate):
        print(f'{candidate._name}: {candidate.count} votes')

    def results(self):
        winner_percentage = self._winner_votes / self._total_votes * 100
        print(f'{self._winner} won: {winner_percentage:.1f}% of votes')

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