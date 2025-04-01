import random
import math

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

    def __init__(self, lower_bound, upper_bound):
        self._lower_bound = lower_bound
        self._upper_bound = upper_bound
        self._guesses = int(math.log2(upper_bound - lower_bound + 1)) + 1
        self._magic_number = random.randint(lower_bound, upper_bound)

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
            print(f'You have {self._guesses} guesses remaining.')
            guess = self.get_guess()
            self._guesses -= 1
            win_result = self._print_feedback(guess)
            if win_result:
                return
            
        print('You have no more guesses. You lost!')

            
    def get_guess(self):
        while True:
            guess = int(input(f'Enter a number between {self._lower_bound} '
                          f'and {self._upper_bound}: '))
            if self._is_valid_guess(guess):
                return guess

    def _is_valid_guess(self, guess):
        if not self._lower_bound <= guess <= self._upper_bound:
            print('Invalid guess. ', end='')
            return False
        return True

    def _print_feedback(self, guess):
        if guess > self._magic_number:
            print('Your guess is too high.')
        elif guess < self._magic_number:
            print('Your guess is too low.')
        else:
            print('That\'s the number!')
            return True



game = GuessingGame(501, 1500)
game.play()