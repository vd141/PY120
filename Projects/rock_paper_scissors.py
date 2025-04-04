'''
OOP RPS
'''

import random

class Player:
    '''
    defines game choices
    '''
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self):
        self.move = None

class Computer(Player):
    '''
    Computer player definition
    '''
    def __init__(self):
        '''
        initialize computer move state
        '''
        super().__init__()

    def choose(self):
        '''
        selects a random choice
        '''
        self.move = random.choice(Player.CHOICES)

    @property
    def move(self):
        '''
        returns the _move attribute
        '''
        return self._move

    @move.setter
    def move(self, move):
        '''
        sets the _move attribute
        '''
        self._move = move

class Human(Player):
    '''
    huamn player definition
    '''
    def __init__(self):
        '''
        initialize human move state
        '''
        super().__init__()

    def choose(self):
        '''
        prompts the user to make a choice (must be a valid choice)
        '''
        while True:
            prompt = 'Select (rock), (paper), or (scissors): '
            choice = input(prompt)
            if choice in Player.CHOICES:
                break
            print('Invalid choice. ', end='')
        self.move = choice

    @property
    def move(self):
        '''
        returns the _move attribute
        '''
        return self._move

    @move.setter
    def move(self, move):
        '''
        sets the _move attribute
        '''
        self._move = move

class RPSGame:
    '''
    controls game flow and collaborates with Human and Computer Players
    '''
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _display_winner(self):
        '''
        compare player choice to computer choice
        '''

        print(f'You chose {self._human.move}.')
        print(f'The computer chose {self._computer.move}.')

        if self._human_wins():
            print('You win!')
        elif self._computer_wins():
            print('Computer wins!')
        else:
            print('It\'s a tie!')

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((human_move == 'rock' and computer_move == 'scissors') or
            (human_move == 'paper' and computer_move == 'rock') or
            (human_move == 'scissors' and computer_move == 'paper'))

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((computer_move == 'rock' and human_move == 'scissors') or
            (computer_move == 'paper' and human_move == 'rock') or
            (computer_move == 'scissors' and human_move == 'paper'))

    def _play_again(self):
        prompt = 'Would you like to play again? y/n: '
        return input(prompt).lower().startswith('y')

    def play(self):
        '''
        dictates game flow
        '''
        self._display_welcome_message()

        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not self._play_again():
                break
        self._display_goodbye_message()

RPSGame().play()
