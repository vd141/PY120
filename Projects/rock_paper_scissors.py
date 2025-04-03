'''
OOP RPS
'''
import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self):
        pass

class Computer(Player):
    def __init__(self):
        self.move = None

    def choose(self):
        self.move = random.choice(Player.CHOICES)

    @property
    def move(self):
        return self._move
    
    @move.setter
    def move(self, move):
        self._move = move

class Human(Player):
    def __init__(self):
        self.move = None

    def choose(self):
        while True:
            prompt = 'Select (rock), (paper), or (scissors): '
            choice = input(prompt)
            if choice in Player.CHOICES:
                break
            print('Invalid choice. ', end='')
        self.move = choice

    @property
    def move(self):
        return self._move
    
    @move.setter
    def move(self, move):
        self._move = move

class RPSGame:
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
        human_move = self._human.move
        computer_move = self._computer.move
        print(f'You chose {human_move}.')
        print(f'The computer chose {computer_move}.')

        # player wins
        if ((human_move == 'rock' and computer_move == 'scissors') or
            (human_move == 'paper' and computer_move == 'rock') or
            (human_move == 'scissors' and computer_move == 'paper')):
            
            print('You win!')
        # computer wins
        elif ((computer_move == 'rock' and human_move == 'scissors') or
            (computer_move == 'paper' and human_move == 'rock') or
            (computer_move == 'scissors' and human_move == 'paper')):

            print('Computer wins!')
        # tie
        else:
            print('It\'s a tie!')

    def _play_again(self):
        prompt = 'Would you like to play again? y/n: '
        return input(prompt).lower().startswith('y')
         

    def play(self):
        self._display_welcome_message()

        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not self._play_again():
                break
        self._display_goodbye_message()

RPSGame().play()