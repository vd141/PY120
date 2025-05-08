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
import random
import os
import time

class PromptMixIn:
    '''
    format prompt for output to console
    '''
    def prompt(self, *messages):
        '''
        takes a message argument of any number of strings and adds ==> to front
        '''
        return f'==> {''.join(messages)}'

    def join_or(self, iterable, separator=', ', final='or'):
        '''
        returns a string: '1, 2, 3, 4, 5, or 6'

        if len(iterable) is 1 , return that element

        if len(iterable) is 2, return those two elements separated by final

        if len(iterable) is greater than 2, return those elements separated by 
        commas, oxford, and final
        '''

        output_str = ''

        try:
            if len(iterable) <= 1:
                output_str += str(iterable[0])
            elif len(iterable) == 2:
                output_str += ' '.join([str(iterable[0]), final, str(iterable[1])])
            elif len(iterable) > 2:
                for item in iterable[:-2]:
                    output_str += str(item)
                    output_str += separator
                output_str += str(iterable[-2]) + separator + final + ' ' + str(iterable[-1])
            return output_str
        except IndexError as e:
            print(f'Iterable must contain at least 1 element: {e}')

# print(PromptMixIn().join_or([1, 2]))

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
    CENTER = 5

    def __init__(self):
        self.available_spaces = list(Board.SPACES)
        self.occupied_spaces = []
        self.squares = {key: ' ' for key in range(1,10)}

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
        self._squares = other

    def print_template(self):
        print(self.prompt('This is the game board. You can pick a position'),
              'by entering its number when prompted.')
        for row in Board.TEMPLATE_BOARD:
            print(row)

    def print_playing_board(self):
        for row in self.playing_board:
            print(row)

    def update_playing_board(self, marker, player_position_choice):
        '''
        STUB
        algorithm to update playing board with player's position choice

        look in template for position of selected position
        get index (row, col) of selected position
        replace position in the playing_board
        '''
        self.squares[player_position_choice] = marker

        self.playing_board = [
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
    tracks score, marker, and occupied positions
    '''
    def __init__(self):
        self.score = 0
        self.marker = None
        self.positions = set()

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

    @property
    def positions(self):
        return self._positions

    @positions.setter
    def positions(self, other):
        self._positions = other

class Human(Player):
    '''
    prompts user at CLI to enter an available position.
    '''
    def select_position(self, board, opponent_positions=None):
        '''
        prompts user to select an available position

        unused parameter left as is for polymorphism
        '''
        available = board.available_spaces
        while available:
            try:
                choice = int(input(self.prompt('Please choose an available ',
                                           f'position: {self.join_or(available)}: ')))
                if choice in available:
                    available.remove(choice)
                    print(self.prompt(f'{self.__class__.__name__} selected {choice}.'))
                    self.positions.add(choice)
                    os.system('clear')
                    return choice
            except ValueError as e:
                print(self.prompt(f'{e}. Input must be an available integer!'))

class Computer(Player):
    '''
    prompts computer to select a position using an offensive, defensive, center,
    or random strategy

    randomly selects from an available position
    '''
    def select_position(self, board, opponent_positions):
        available = board.available_spaces
        if available:
            print(self.prompt('Computer deciding...'))
            time.sleep(2)
            choice = self._offensive_computer_move(available, self.positions)
            if not choice:
                choice = self._defensive_computer_move(available,
                                                      opponent_positions)
            if not choice:
                choice = self._pick_center(available)
            if not choice:
                choice = random.choices(available)[0]
            available.remove(choice)
            self.positions.add(choice)
            os.system('clear')
            print(self.prompt(f'{self.__class__.__name__} selected {choice}.'))
            return choice

    def _offensive_computer_move(self, available, self_positions):
        return self._computer_ai_choice(available, self_positions)

    def _defensive_computer_move(self, available, opponent_positions):
        return self._computer_ai_choice(available, opponent_positions)

    def _computer_ai_choice(self, available, current_positions):
        '''
        feed opponent positions into current_positions for defensive strategy
        feed self's positions into current_positions for offensive strategy
        '''
        winning_combos = TTTGame.WINNING_CONDITIONS

        for combo in winning_combos:
            intersection = combo.intersection(current_positions)
            if len(intersection) == 2:
                next_choice = list(combo - intersection)[0]
                if next_choice in available:
                    return next_choice
        return None

    def _pick_center(self, available):
        if Board.CENTER in available:
            return Board.CENTER
        return None


class TTTGame(PromptMixIn):
    '''
    handles game flow and attributes
    '''
    WINNING_CONDITIONS = [
            {1, 5, 9},
            {3, 5, 7},
            {1, 4, 7},
            {2, 5, 8},
            {3, 6, 9},
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9},
        ]

    PLAYER_ONE_MARKER = 'O'
    PLAYER_TWO_MARKER = 'X'
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
        self.board = self._initialize_board()
        self.player_score = 0
        self.computer_score = 0
        self.p1 = None
        self.p2 = None

    @property
    def player_score(self):
        return self._player_score

    @player_score.setter
    def player_score(self, score):
        self._player_score = score

    @property
    def computer_score(self):
        return self._computer_score

    @computer_score.setter
    def computer_score(self, score):
        self._computer_score = score

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
        self._clear_console()
        self._display_welcome_message()
        self._reading_seconds(2)
        self._initialize_board()
        while True:
            self._play_a_game()
            self._print_score()
            winner = self._best_of_three()
            if winner:
                print(self.prompt(f'{winner} won the match!'))
                break
            if not self._play_another_game():
                break
        self._display_goodbye_message()
        self._reading_seconds(2)
        self._clear_console()

    def _play_a_game(self):
        self._clear_console()
        self.board.print_template()
        self._reading_seconds(4)
        self._select_starter_random()
        self._set_player_marker()
        self._print_starting_players()
        self._reading_seconds(5)
        self._initialize_board()

        while self.board.available_spaces:
            p1_choice = self.p1.select_position(self.board, self.p2.positions)
            self.board.update_playing_board(self.p1.marker, p1_choice)
            self._clear_console()
            self.board.print_playing_board()
            if self._is_winning_condition(self.p1):
                self._tally_score(self.p1)
                self._print_winner(self.p1)
                self._reading_seconds(2)
                self._clear_console()
                return
            p2_choice = self.p2.select_position(self.board, self.p1.positions)
            self.board.update_playing_board(self.p2.marker, p2_choice)
            self._clear_console()
            self.board.print_playing_board()
            if self._is_winning_condition(self.p2):
                self._tally_score(self.p2)
                self._print_winner(self.p2)
                self._reading_seconds(2)
                self._clear_console()
                return

        self._print_tie()

    def _play_another_game(self):
        while True:
            user_decision = input(self.prompt('Would you like to play another '
                                              'game? y/n ')).lower()
            if user_decision in ['y', 'n']:
                if user_decision == 'y':
                    return True
                return False
            print(self.prompt('Input must be either y/n!'))

    def _clear_console(self):
        os.system('clear')

    def _display_welcome_message(self):
        print(self.prompt('Welcome to Tic-Tac-Toe!'))

    def _display_goodbye_message(self):
        print(self.prompt('Thanks for playing. Goodbye!'))

    def _reading_seconds(self, seconds):
        time.sleep(seconds)

    def _select_starter_random(self):
        '''
        selects a human or computer instance as the p1/p2
        '''
        players = [Human(), Computer()]
        self.p1 = random.choices(players)[0]
        self.p2 = [player for player in players if
                         player is not self.p1][0]

    def _set_player_marker(self):
        self.p1.marker, self.p2.marker = self.PLAYER_ONE_MARKER, self.PLAYER_TWO_MARKER

    def _print_starting_players(self):
        print(self.prompt(f'Player 1 is {self.p1.__class__.__name__}: '
                          f'{self.p1.marker}'))
        print(self.prompt('Player 2 is ',
                          f'{self.p2.__class__.__name__}: '
                          f'{self.p2.marker}'))
        print(self.prompt('Player 1 will make the first move.'))

    def _initialize_board(self):
        self.board = Board()

    def _is_winning_condition(self, player):
        '''
        winning conditions are
        diagonals: 1-5-9, 3-5-7
        verticals: 1-4-7, 2-5-8, 3-6-9
        horizontals: 1-2-3, 4-5-6, 7-8-9

        check to see if any set of these is in the set of player positions. if 
        yes, player wins
        '''

        for three_in_row in self.WINNING_CONDITIONS:
            if player.positions.issuperset(three_in_row):
                return True

        return False

    def _tally_score(self, player):
        if isinstance(player, Human):
            self.player_score += 1
        if isinstance(player, Computer):
            self.computer_score += 1

    def _print_score(self):
        print(self.prompt(f'Human\'s score is {self.player_score}. '
                          f'Computer\'s score is {self.computer_score}'))

    def _print_winner(self, player):
        print(self.prompt(f'{player.__class__.__name__} wins!'))

    def _print_tie(self):
        print('All moves exhausted. It\'s a tie!')

    def _best_of_three(self):
        if self._player_score == 3:
            return 'Human'
        if self._computer_score == 3:
            return 'Computer'
        return None

game = TTTGame()
game.play()
