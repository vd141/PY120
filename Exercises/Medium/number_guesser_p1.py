'''
create an OOP number guessing class for numbers in the range 1 to 100
with a limit of 7 guesses per game

checks for invalid guess. if guess is invalid, reprompt for guess but do not subtract
from allotted guesses

each valid guess deducts an attempt from the total allotted attempts
'''

import random

class GuessingGame:

    LOW_BOUND = 1
    HIGH_BOUND = 100

    def __init__(self):
        self._remaining_attempts = 7
        self._magic_number = random.randint(GuessingGame.LOW_BOUND, 
                                            GuessingGame.HIGH_BOUND)

    def play(self):
        while self._remaining_attempts > 0:
            print(f'You have {self._remaining_attempts} guesses remaining.')
            while True:
                guess = self._capture_guess()
                if self._valid_guess(guess):
                    break
            if self._winning_guess_feedback(guess):
                break
            else:
                self._remaining_attempts -= 1

        if self._remaining_attempts == 0:
            print('You have no more guesses. You lost!')

    def _winning_guess_feedback(self, guess):
        '''
        give feedback about guess

        returns true if guess is correct, False otherwise
        '''
        if guess < self._magic_number:
            print('Your guess is too low.')
            return False
        elif guess > self._magic_number:
            print('Your guess is too high.')
            return False
        else:
            print('That\'s the number!')
            print('You won!')
            return True

    def _capture_guess(self):
        return int(input(f'Enter a number between {GuessingGame.LOW_BOUND} and {GuessingGame.HIGH_BOUND}: '))

    def _valid_guess(self, guess):
        if guess not in range(GuessingGame.LOW_BOUND, GuessingGame.HIGH_BOUND + 1):
            print('Invalid guess. ', end='')
            return False
        return True

game = GuessingGame()
game.play()