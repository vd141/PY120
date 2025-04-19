'''
OOO Tic tac toe

3 steps:
1. textual description of game
2. extract significant nouns and verbs from description
3. organize and associate the verbs with nouns

1. 
- in tic tac toe, there is a 3x3 board
- there are two players (computer, human)
- the starting player is randomly selected
- the starting player can place a piece anywhere on the board
- once the player finishes the turn, the other player can place a piece wherever
there isn't already a piece
- players continue to swap turns until
    - the board is filled
    - a player wins
    - a player wins if their pieces are 3-in a row/column/diagonal


2. extract significant nouns and verbs from description
    - nouns
        - game 
            - turn
            - winning conditions
                - 3 in a row
                - 3 in a column
                - 3 in a diag
            - tie conditions
            - board is filled and no winning conditions
        - board
            - available spaces
            - occupied spaces
        - player (human, computer)
            - piece
        - move
    
    = verbs
        - initialize board
        - display board
        - select starting player (and assign starting piece)
        - place a piece
            - computer choose a strategy
            - player class gets input from player
        - refresh board display
        - check for stopping conditions
            - check for winning condition
            - check for tie condition
        - prompt player for another game if one is so desired


3. associate nouns with verbs
    - board
        - initialize board
            - initialize available spaces
            - initialize occupied spaces
        - refresh/print board
    - game
        - initialize board
        - initialize winning conditions (const?)
        - select starting player
        - assign starting piece
        - check for stopping conditions
            - check for winning condition
            - check for tie condition
        - prompt player for another game if one is so desired
    - player
        - select a piece
        - place a piece

'''

'''
scaffolding
'''

import random
import os

class PromptMixIn:
    def prompt(self, *messages):
        return f'==> {''.join(messages)}'

class Board(PromptMixIn):
    '''
    functionality:
        - initialize board
            - initialize available spaces
            - initialize occupied spaces
        - refresh/print board
    '''
    SPACES = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    TEMPLATE_BOARD = [
        '+-----------------+',
        '|  1  |  2  |  3  |',
        '+-----------------+',
        '|  4  |  5  |  6  |',
        '+-----------------+',
        '|  7  |  8  |  9  |',
        '+-----------------+'
    ]
    EMPTY_BOARD = [
        '+-----------------+',
        '|     |     |     |',
        '+-----------------+',
        '|     |     |     |',
        '+-----------------+',
        '|     |     |     |',
        '+-----------------+'
    ]

    def __init__(self):
        self.available_spaces = list(Board.SPACES)
        self.occupied_spaces = list()
        self.squares = {
            1: ' ',
            2: ' ',
            3: ' ',
            4: ' ',
            5: ' ',
            6: ' ',
            7: ' ',
            8: ' ',
            9: ' ',
        }
        self.playing_board = self.update_playing_board()

    @property
    def available_spaces(self):
        return self._available_spaces
    
    @available_spaces.setter
    def available_spaces(self, other):
        self._available_spaces = other

    @property
    def occupied_spaces(self):
        return self._occupied_spaces
    
    @occupied_spaces.setter
    def occupied_spaces(self, other):
        self._occupied_spaces = other

    @property
    def playing_board(self):
        return self._player_board
    
    @playing_board.setter
    def playing_board(self, other):
        self._player_board = other

    @property
    def squares(self):
        return self._squares
    
    @squares.setter
    def squares(self, other):
        print('I\'ve been modified!')
        self._squares = other

    def print_template(self):
        print(self.prompt('This is the game board. You can pick a position'),
              'by entering its number when prompted.')
        for row in Board.TEMPLATE_BOARD:
            print(row)

    def print_playing_board(self):
        for row in self.playing_board:
            print(row)

    def update_playing_board(self):
        '''
        STUB
        algorithm to update playing board with player's position choice

        look in template for position of selected position
        get index (row, col) of selected position
        replace position in the playing_board
        '''
        print(self.squares)
        return [
            '+-----------------+',
            f'|  {self.squares[1]}  |  {self.squares[2]}  |  {self.squares[3]}  |',
            '+-----------------+',
            f'|  {self.squares[4]}  |  {self.squares[5]}  |  {self.squares[6]}  |',
            '+-----------------+',
            f'|  {self.squares[7]}  |  {self.squares[8]}  |  {self.squares[9]}  |',
            '+-----------------+'
        ]

class Player(PromptMixIn):
    '''
    select a piece
    place a piece
    '''
    def __init__(self):
        self.score = 0
        self.marker = None
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, other):
        self._score = other

    @property
    def marker(self):
        return self._marker
    
    @marker.setter
    def marker(self, other):
        self._marker = other

class Human(Player):
    def select_position(self, board):
        available = board.available_spaces
        while True:
            choice = input(self.prompt('Please choose an available ',
                                           f'position: {available}: '))
            try:
                if int(choice) in available:
                    return int(choice)
            except ValueError as e:
                print(self.prompt(f'{e}. Input must be an available integer!'))

class Computer(Player):
    def select_position(self, board):
        available = board.available_spaces
        return random.choices(available)[0]


class TTTGame(PromptMixIn):
    '''
    orchestration engine

        - initialize board
        - initialize winning conditions (const?)
        - select starting player
        - assign starting piece
        - check for stopping conditions
            - check for winning condition
            - check for tie condition
        - prompt player for another game if one is so desired
    '''
    def __init__(self):
        '''
        STUB
        '''
        pass

    def play(self):
        '''
        SPIKE

        - display a welcome message
        - initialize players
        - randomly select first player
        - display first player
        - create instance of board
        - display board template
        - repeat the following:
            - get first player choice
                - if player is human, display possible options 
                - update board if valid choice
                - display board
            - get second player choice
                - update board if valid choice
                - display board
            - evaluate winning or tie condition
                - exit and display appropriate message if condition met
        - display end game message
        '''
        self._display_welcome_message()
        p1, p2 = self._randomly_select_starter()
        game_board = Board()
        game_board.print_template()
        while True:
            p1_choice = p1.select_position(game_board)
            p2_choice = p2.select_position(game_board)

            print(type(p1_choice))
            game_board.squares[p1_choice] = 'O'
            game_board.update_playing_board()
            print(game_board.squares)

            if p1_choice and p2_choice:
                break

        game_board.print_playing_board()

    def _randomly_select_starter(self):
        '''
        selects a human or computer instance as the p1/p2 and sets marker for
        each player 'O' for starter, 'X' for p2
        '''
        players = [Human(), Computer()]
        first_player = random.choices(players)[0]
        second_player = [player for player in players if 
                         player is not first_player][0]
        first_player.marker, second_player.marker = 'O', 'X'
        print(self.prompt(f'First player is {first_player.__class__.__name__}: '
                          f'{first_player.marker}'))
        print(self.prompt('Second player is ',
                          f'{second_player.__class__.__name__}: '
                          f'{second_player.marker}'))
        return first_player, second_player

    def _display_welcome_message(self):
        print(self.prompt('Welcome to Tic-Tac-Toe!'))

    def _refresh_display_with_template(self, game_board):
        os.system('clear')
        game_board.print_template_board()

game = TTTGame()
game.play()
