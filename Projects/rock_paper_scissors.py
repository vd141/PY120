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

    def choose(self):
        '''
        weight scissors 5, all others 1 (random.choices normalizes weights)
        '''

        weights = [5 if isinstance(choice, Scissors) else 1 for choice in
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
            prompt = f'Select a move from {list(Player.CHOICES.keys())}: '
            choice = input(prompt)
            if choice in Player.CHOICES:
                break
            print('Invalid choice. ', end='')
        self.move = Player.CHOICES[choice]


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
        self._reference_player_history_if_daneel()
        print(f'Your opponent is: {type(self._computer).__name__}')

    def _reference_player_history_if_daneel(self):
        if isinstance(self._computer, Daneel):
            self._computer.track_human_history(self._human.move_history)

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

'''
Keeping score: class or state?
    - a score doesn't need to do anything.
    - we just need to access the score to display it, update it after each round
      and check it when deciding to end the game
    - each player has its own score -> we can make the score an attribute of the
      player class
'''

'''
Adding lizard and spock:
    - add to the player class
    - need to update winning logic
    - 
'''

'''
Player holds an instance of each possible choice class in the tuple


add a move parent class
and each possible move is a subclass of the move parent
each move has a victim. victims are stored as move states
each move has weaknesses. weaknesses are stored as move states

for each subclass, the compare method checks if the other class being compared
is a victim. if it is, return True. else, return false. but a move isn't doing the
comparing. thhe game is. so let the game handle the comparison
    - game comparison compares the moves of the two players
    - if type of human choice is a victim of computer choice, computer wins and vice versa
    - if types of both choices are the same, it's a tie

    - can we compare types without creating an instance of a type? yes, by using
    isinstance

player selects a string, code will select corresponding Move instance

converting moves to separate classes required updating the code in several places. but
the code looks more readable/organized. introducing a new move would require updates
to the Human.choose() method. But otherwise, no changes are needed
'''

'''
keep track of a history of moves

use a list to keep track of each player's moves. the record can be an attribute
of the player class. updates to the move attribute will be added to the list.

when the move setter is invoked, update move history
'''

'''
computer personalities

R2D2 always chooses rock
HAL tends to choose scissors more often than others
Daneel always chooses your previous move (first move is random)

it makes more sense to make the additional robots subclasses of player rather
than computer because computer is definied solely by its ability to choose randomly
'''
