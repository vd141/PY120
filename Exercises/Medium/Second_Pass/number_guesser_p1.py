import random

'''
create an OOP number guessing class for numbers in the range from 1 to 100,
with a limit of 7 guesses per game. the game should play like this

game = GuessingGame()
game.play()

You have 7 guesses remaining.
Enter a number between 1 and 100: 104
Invalid guess. Enter a number between 1 and 100: 50
Your guess is too low.

You have 6 guesses remaining.
Enter a number between 1 and 100: 75
Your guess is too low.

You have 5 guesses remaining.
Enter a number between 1 and 100: 85
Your guess is too high.

You have 4 guesses remaining.
Enter a number between 1 and 100: 0
Invalid guess. Enter a number between 1 and 100: 80
Your guess is too low.

You have 3 guesses remaining.
Enter a number between 1 and 100: 81
That's the number!

You won!

game.play()

You have 7 guesses remaining.
Enter a number between 1 and 100: 50
Your guess is too high.

You have 6 guesses remaining.
Enter a number between 1 and 100: 25
Your guess is too low.

You have 5 guesses remaining.
Enter a number between 1 and 100: 37
Your guess is too high.

You have 4 guesses remaining.
Enter a number between 1 and 100: 31
Your guess is too low.

You have 3 guesses remaining.
Enter a number between 1 and 100: 34
Your guess is too high.

You have 2 guesses remaining.
Enter a number between 1 and 100: 32
Your guess is too low.

You have 1 guess remaining.
Enter a number between 1 and 100: 32
Your guess is too low.

You have no more guesses. You lost!
'''

class GuessingGame:

    GUESSES = 7
    LOWER_BOUND = 1
    UPPER_BOUND = 100

    def __init__(self):
        self._guesses = GuessingGame.GUESSES
        self._magic_number = random.randint(GuessingGame.LOWER_BOUND, GuessingGame.UPPER_BOUND)
        pass

    def play(self):
        '''
        each loop; while number of guesses is above 0
            - print number of guesses remaining
            - get user guess
            - validate guess
            - print feedback message. if guess correct, return
            - subtract 1 from guesses remaining
        '''
        while self._guesses > 0:
            print(f'You have {self._guesses} remaining.')
            guess = self.get_guess()
            
    def get_guess(self):
        while True:
            guess = input(f'Enter a number between {GuessingGame.LOWER_BOUND} '
                          f'and {GuessingGame.UPPER_BOUND}: ')
            if GuessingGame._is_valid_guess(guess):
                return guess

    @classmethod
    def _is_valid_guess(cls, guess):
        if not cls.LOWER_BOUND < guess < cls.UPPER_BOUND:
            print('Invalid guess.', end='')
            return False
        return True

    def print_feedback(self, guess):
        pass



game = GuessingGame()
game.play()