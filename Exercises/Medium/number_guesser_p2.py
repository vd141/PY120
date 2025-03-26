import random

class GuessingGame:
    SECRET_RANGE = range(1, 100 + 1)
    MAX_GUESSES = 7
    GUESSES_REMAINING = range(MAX_GUESSES, 0, -1)

    RESULT_OF_GUESS_MESSAGE = {
        'high':  "Your number is too high.",
        'low':   "Your number is too low.",
        'match': "That's the number!",
    }

    WIN_OR_LOSE = {
        'high':  'lose',
        'low':   'lose',
        'match': 'win',
    }

    RESULT_OF_GAME_MESSAGE = {
        'win':  "You won!",
        'lose': "You have no more guesses. You lost!",
    }

    def __init__(self):
        self.secret_number = None

    def play(self):
        self.reset()
        game_result = self.play_game()
        self.show_game_end_message(game_result)

    def reset(self):
        self.secret_number = random.choice(self.SECRET_RANGE)

    def play_game(self):
        for remaining_guesses in self.GUESSES_REMAINING:
            self.show_guesses_remaining(remaining_guesses)
            result = self.check_guess(self.get_one_guess())
            print(self.RESULT_OF_GUESS_MESSAGE[result])
            if result == 'match':
                return self.WIN_OR_LOSE[result]

        return self.WIN_OR_LOSE[result]

    def show_guesses_remaining(self, remaining):
        print()
        if remaining == 1:
            print('You have 1 guess remaining.')
        else:
            print(f"You have {remaining} guesses remaining.")

    def get_one_guess(self):
        while True:
            prompt = ("Enter a number between "
                      f"{self.SECRET_RANGE[0]} and "
                      f"{self.SECRET_RANGE[-1]}: ")

            guess = input(prompt)
            if guess.isdigit():
                guess = int(guess)
                if guess in self.SECRET_RANGE:
                    return guess

            print("Invalid guess. ", end="")

    def check_guess(self, guess_value):
        if guess_value == self.secret_number:
            return 'match'
        elif guess_value < self.secret_number:
            return 'low'
        else:
            return 'high'

    def show_game_end_message(self, result):
        print("\n", self.RESULT_OF_GAME_MESSAGE[result])