'''
Q1

update this code os Bingo inherits play from the game class
'''
class Game:
    count = 0

    def __init__(self, game_name, player1):
        Game.count += 1
        self._game_name = game_name
        self._player1 = player1

    def play(self):
        return f'Start the {self.__class__.__name__} game!'

class Bingo(Game):
    @property
    def player_name(self):
        return self._player1

class Scrabble(Game):
    def __init__(self, game_name, player1, player2):
        super().__init__(game_name, player1)
        self._player2 = player2
    
    @property
    def player_name1(self):
        return self._player1
    
    @property
    def player_name2(self):
        return self._player2

'''
Q2

update previous code so the following works
'''
bingo = Bingo('Bingo', 'Bill')
print(Game.count)                       # 1
print(bingo.play())                     # Start the Bingo game!
print(bingo.player_name)                # Bill

scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
print(Game.count)                       # 2
print(scrabble.play())                  # Start the Scrabble game!
print(scrabble.player_name1)            # Jill
print(scrabble.player_name2)            # Sill
print(scrabble.player_name)
# AttributeError: 'Scrabble' object has no attribute 'player_name'


'''
3. Benefits of using OOP in Python?
    - reduce redundant code
    - 
'''