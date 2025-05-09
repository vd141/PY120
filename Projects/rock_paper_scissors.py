'''
OOP RPS
'''

import random

class Move:
    '''
    move superclass for possible player moves

    Weaknesses are unused in this implementation of RPS, but are left as a 
    reference and for potential future use

    scissors beats 
    paper beats 
    rock beats 
    lizard beats 
    spock beats
    scissors beats
    lizard beats
    paper beats
    spock beats
    rock beats
    scissors

    human wins if computer choice is in human choice's victims
    '''
    def __init__(self):
        self._victims = []
        self._weaknesses = []

    @property
    def victims(self):
        '''
        victims getter
        '''
        return self._victims

    @property
    def weaknesses(self):
        '''
        weaknesses getter
        '''
        return self._weaknesses


class Rock(Move):
    '''
    rock move's victims and weaknesses
    '''
    def __init__(self):
        super().__init__()
        self._victims = [Scissors, Lizard]
        self._weaknesses = [Paper, Spock]


class Paper(Move):
    '''
    paper move's victims and weaknesses
    '''
    def __init__(self):
        super().__init__()
        self._victims = [Rock, Spock]
        self._weaknesses = [Scissors, Lizard]


class Scissors(Move):
    '''
    scissor's victims and weaknesses
    '''
    def __init__(self):
        super().__init__()
        self._victims = [Paper, Lizard]
        self._weaknesses = [Rock, Spock]


class Lizard(Move):
    '''
    lizard's victims and weaknesses
    '''
    def __init__(self):
        super().__init__()
        self._victims = [Spock, Paper]
        self._weaknesses = [Rock, Scissors]


class Spock(Move):
    '''
    spock's victims and weaknesses
    '''
    def __init__(self):
        super().__init__()
        self._victims = [Scissors, Rock]
        self._weaknesses = [Paper, Lizard]


class Player:
    '''
    defines game choices
    '''
    CHOICES = {'rock': Rock(),
               'paper': Paper(),
               'scissors': Scissors(),
               'lizard': Lizard(),
               'spock': Spock(),
               }

    ABBREVIATIONS = {'r': 'rock',
                     'p': 'paper',
                     'sc': 'scissors',
                     'l': 'lizard',
                     'sp': 'spock',
                     }

    CHOICES_FORMAT = ['(r)ock',
                      '(p)aper',
                      '(sc)issors',
                      '(l)izard',
                      '(sp)ock',
                      ]

    def __init__(self):
        self.move_history = []
        self.move = None
        self.score = 0

    @property
    def move_history(self):
        '''
        move_history getter
        '''
        return self._move_history

    @move_history.setter
    def move_history(self, move_history_update):
        '''
        move_history setter
        '''
        self._move_history = move_history_update

    @property
    def move(self):
        '''
        move getter
        '''
        return self._move

    @move.setter
    def move(self, new_move):
        '''
        move setter
        '''
        self._move = new_move
        self.move_history.append(type(new_move).__name__)
        if 'NoneType' in self.move_history:
            self.move_history.remove('NoneType')

    @property
    def score(self):
        '''
        score getter
        '''
        return self._score

    @score.setter
    def score(self, new_score):
        '''
        score setter
        '''
        self._score = new_score

    def track_human_history(self, _):
        '''
        dummy method (overriden by Daneel class)
        '''
        pass


class Computer(Player):
    '''
    Computer player definition
    '''

    def choose(self):
        '''
        selects a random choice
        '''
        self.move = random.choice(list(Player.CHOICES.values()))


class R2D2(Player):
    '''
    always chooses rock
    '''

    def choose(self):
        '''
        selects rock
        '''
        self.move = Player.CHOICES['rock']


class HAL(Player):
    '''
    tends to choose scissors more than others
    '''
    SCISSOR_WEIGHT = 5
    OTHER_WEIGHT = 1

    def choose(self):
        '''
        weight scissors 5, all others 1 (random.choices normalizes weights)
        '''

        weights = [HAL.SCISSOR_WEIGHT if isinstance(choice, Scissors) else
                   HAL.OTHER_WEIGHT for choice in
                   Player.CHOICES.values()]

        self.move = random.choices(list(Player.CHOICES.values()),
                                   weights=weights, k=1)[0]


class Daneel(Player):
    '''
    always chooses player's previous choice
    '''
    def __init__(self):
        '''
        initialize computer move state
        '''
        super().__init__()
        self._other_move_history = None

    def track_human_history(self, move_history):
        '''
        tracks user's move history
        '''
        self._other_move_history = move_history

    def choose(self):
        '''
        needs access to player's choice history
        '''
        if len(self._other_move_history) == 1:
            self.move = random.choice(list(Player.CHOICES.values()))
        else:
            print(self._other_move_history)
            self.move = Player.CHOICES[self._other_move_history[-2].lower()]


class Human(Player):
    '''
    huamn player definition
    '''

    def choose(self):
        '''
        prompts the user to make a choice (must be a valid choice)
        '''
        while True:
            prompt = f'Select a move from {Player.CHOICES_FORMAT}: '
            choice = input(prompt).lower()
            if choice in Player.ABBREVIATIONS:
                break
            print('Invalid choice. ', end='')
        self.move = Player.CHOICES[Player.ABBREVIATIONS[choice]]


class RPSGame:
    '''
    controls game flow and collaborates with Human and Computer Players
    '''

    AVAILABLE_PLAYERS = {
        'r2d2': R2D2(),
        'hal': HAL(),
        'daneel': Daneel(),
        'computer': Computer(),
    }

    def __init__(self):
        self._human = Human()
        self._computer = None

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _select_opponent(self):
        available_players = list(RPSGame.AVAILABLE_PLAYERS.keys())
        prompt = f'Select an opponent from the list: {available_players}: '
        while True:
            user_selection = input(prompt).lower()
            if user_selection in available_players:
                break
            print('Invalid selection. ', end='')

        self._computer = RPSGame.AVAILABLE_PLAYERS[user_selection]
        self._computer.track_human_history(self._human.move_history)
        print(f'Your opponent is: {type(self._computer).__name__}')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _display_winner(self):
        '''
        compare player choice to computer choice
        '''

        print(f'You chose {type(self._human.move).__name__}.')
        print(f'{type(self._computer).__name__} chose '
              f'{type(self._computer.move).__name__}.')

        winner = self._determine_winner()

        if winner:
            print(f'{type(winner).__name__} wins!')
        else:
            print('It\'s a tie!')
        self._display_score()

        print(f'Your choice history: {self._human.move_history}')
        print(f'Computer choice history: {self._computer.move_history}')

    def _display_score(self):
        print(f'Your score is: {self._human.score}, '
              f'{type(self._computer).__name__}\'s score '
              f'is: {self._computer.score}')

    def _determine_winner(self):
        human_move = self._human.move
        computer_move = self._computer.move

        if type(computer_move) in human_move.victims:
            self._human.score += 1
            return self._human
        if type(human_move) in computer_move.victims:
            self._computer.score += 1
            return self._computer
        return None

    def _play_again(self):
        prompt = 'Would you like to play again? y/n: '
        return input(prompt).lower().startswith('y')

    def _reached_five(self):
        return 5 in (self._computer.score, self._human.score)

    def play(self):
        '''
        dictates game flow
        '''
        self._display_welcome_message()
        self._select_opponent()

        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if self._reached_five() or not self._play_again():
                break
        self._display_goodbye_message()


RPSGame().play()
