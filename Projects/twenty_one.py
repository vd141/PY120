'''
1. write a textual description of the problem or exercise
    - card game with a dealer and a player
    - deck has 52 cards
    - participants try to get as close to 21 as possible without going over
    - both participants receive two cards
        - dealer hides one of their cards
        - player can see both of their cards
    
    - player takes the first turn and can either hit or stay
    - if the player's hand surpasses 21, the player busts and the dealer wins
    - if the player stays, the dealer plays next

    - if the player didn't bust and chose to stay, it is the dealer's turn
    - dealer reveals face-down card
    - if dealer's hand is under 17, dealer automatically hits
    - dealer busts if hand goes over 21
    - if dealer has 17 points or more, dealer stays

    - results of game are determined

2. extract the significant nouns and verbs from the description
    - nouns 
        - deck
            - 52 cards
            - deal method
            - 
        - card
            - value
            - suit
        - dealer
            - hand
            - points
            - strategy
        - player
            - hand
            - points
            - strategy
        - twenty-one game
            - rules
                - bust
                - 21
            - flow
        
    - additional reqs:
        - welcome message
        - goodbye message
        - when the player has an opportunity to hit or stay:
            - display hand and total
            - display one of dealer's cards
        - when it is the dealer's turn:
            - dealer doesn't play (automatically wins) when player busts
            - show full dealer hand before dealer decides to hit or stay
            - show updated hand if dealer hits
            - display results when dealer stays
        - ask if player wants to play again when game is over
        - player starts with 5 dollars. a win/loss counts +/-1 to the player's
          pot. game ends when the player runs out of money ($0) or becomes rich
          ($10)
        - create a new deck every round

3. organize and associate the verbs with the nouns

4. write scaffolding and spike code
'''
import random
import os
import time

def clear_screen():
    os.system('clear')

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
            return None

class Card:
    '''
    each card has a value and suit attribute
    '''
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

class Deck:
    '''
    initializes a deck of 52 cards. has a draw method
    '''
    SUITS = ["\u2660",  # Spades (♠)
              "\u2665",  # Hearts (♥)
              "\u2666",  # Diamonds (♦)
              "\u2663"]  # Clubs (♣)
    FACES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                  'Jack', 'Queen', 'King']

    def __init__(self):
        self.reset()

    def reset(self):
        values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
        card_names = [f'{face_name} of {suit}' for suit in Deck.SUITS
                                        for face_name in Deck.FACES]
        self._deck = [Card(name, values[index]) for index, name in enumerate(
            card_names)]
        random.shuffle(self._deck)

    def __str__(self):
        return str(list(str(card) for card in self._deck))

    def __len__(self):
        return len(self._deck)

    def draw(self):
        drawn_card = random.choice(self._deck)
        self._deck.remove(drawn_card)
        return drawn_card

class Opponent(PromptMixIn):
    '''
    parent class for player and dealer.

    each opponent has hand and points attributes and a strategy method

    calculates value of hand (decides if A is 1 or 11)

    determines if self has busted

    has a method to display full hand
    '''
    TWENTY_ONE = 21

    def __init__(self):
        self.reset()

    def reset(self):
        self.hand = []
        self.hand_value = 0
        self.has_ace = False

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, new_hand):
        self._hand = new_hand

    @property
    def hand_value(self):
        return self._hand_value

    @hand_value.setter
    def hand_value(self, new_value):
        self._hand_value = new_value

    @property
    def has_ace(self):
        return self._has_ace

    @has_ace.setter
    def has_ace(self, tf):
        self._has_ace = tf

    def add_to_hand(self, card):
        '''
        adds the card to hand and determines the new point value of hand

        determines if incoming card is ace. if so, latches has_ace to true
        '''
        self.hand.append(card)
        self._determine_value(card)

    def _determine_value(self, card):
        card_value = card.value
        if not self.has_ace and card_value == 'Ace':
            self.has_ace = True
            card_value = 11
        elif card_value == 'Ace':
            card_value = 1
        self.hand_value += card_value

    def display_full_hand(self):
        print(self.prompt(f'{self.__class__.__name__}\'s hand is: '
              f'{self.join_or([str(card) for card in self.hand], ', ', 'and')}.'))

    def display_hand_value(self):
        print(self.prompt(f'{self.__class__.__name__}\'s hand value is: {self.hand_value}.'))

    def hit(self, card):
        print(self.prompt(f'{self.__class__.__name__} hits!'))
        self.add_to_hand(card)

    def stay(self):
        print(self.prompt(f'{self.__class__.__name__} stays!'))

    def is_bust(self):
        return self.hand_value > Opponent.TWENTY_ONE

class Dealer(Opponent):
    '''
    dealer has a strategy method, which dictates whether the dealer will hit or
    stay

    has a method to display one card
    '''
    def strategy(self, deck):
        self.display_full_hand()
        self.display_hand_value()
        while True:
            if self.hand_value < 17:
                self.hit(deck.draw())
                self.display_full_hand()
                self.display_hand_value()
                self._reading_pause_seconds(3)
                if self.is_bust():
                    print(self.prompt(f'{self.__class__.__name__} busts!'))
                    break
            else:
                self.stay()
                break

    def show_one(self):
        '''
        displays first card in hand
        '''
        print(self.prompt(f'Dealer shows {self.hand[0]}.'))

    def _reading_pause_seconds(self, seconds):
        time.sleep(seconds)

class Player(Opponent):
    '''
    player has a strategy method, which takes player input (hit or stay)

    player also has a cash attribute, which is initialized to 5
    '''
    def __init__(self):
        super().__init__()
        self.cash = 5

    def strategy(self, deck):
        '''
        shows player hand and value of hand

        asks if player wants to hit or stay. continues asking until player stays or busts

        player can enter h or s to hit or stay
        '''
        self.display_full_hand()
        self.display_hand_value()
        self.hit_or_stay(deck)

    def hit_or_stay(self, deck):
        while True:
            decision = input(self.prompt('Do you want to (h)it or (s)tay? ')).lower()
            if decision in ['h', 's']:
                if decision == 'h':
                    self.hit(deck.draw())
                    self.display_full_hand()
                    self.display_hand_value()
                    if self.is_bust():
                        print(self.prompt(f'{self.__class__.__name__} busts!'))
                        break
                else:
                    self.stay()
                    break
            else:
                print(self.prompt('Input must either be \'h\' or \'s\'!'))

    def is_rich(self):
        return self.cash >= 10

    def is_broke(self):
        return self.cash <= 0

    def display_cash(self):
        print(self.prompt(f'Player has {self.cash} dollars.'))

    def display_cash_condition(self):
        if self.is_broke():
            print(self.prompt(f'{self.__class__.__name__} is broke!'))
        if self.is_rich():
            print(self.prompt(f'{self.__class__.__name__} is rich!'))

    # def is_bust(self):
    #     if super().is_bust:
    #         self.cash -= 1

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, new_cash):
        self._cash = new_cash

class TwentyOne(PromptMixIn):
    '''
    initializes deck and players. dictates game flow. decides a winner

    welcome message

    initialize deck and players

    deal cards to dealer and player

    prompt player for decision

    goodbye message

    '''

    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, new_player):
        self._player = new_player

    @property
    def dealer(self):
        return self._dealer

    @dealer.setter
    def dealer(self, new_dealer):
        self._dealer = new_dealer

    @property
    def deck(self):
        return self._deck

    @deck.setter
    def deck(self, new_deck):
        self._deck = new_deck

    def play(self):
        clear_screen()
        self._welcome_message()
        while not (self.player.is_broke() or self.player.is_rich()):
            self._deal_cards()
            self.dealer.show_one()
            self.player.display_full_hand()
            self.player.display_hand_value()
            self.player.hit_or_stay(self.deck)
            if not self.player.is_bust():
                self.dealer.strategy(self.deck)
            if not self._win_if_bust():
                self._win_score()
            self.player.display_cash()
            self._reset_deck_and_hands()
            self._reading_pause_seconds(3)
            clear_screen()
        self.player.display_cash_condition()
        self._goodbye_message()

    def _deal_cards(self):
        for _ in range(2):
            self.player.add_to_hand(self.deck.draw())
            self.dealer.add_to_hand(self.deck.draw())

    def _win_if_bust(self):
        if self.player.is_bust():
            print(self.prompt(f'{self.dealer.__class__.__name__} wins!'))
            self.player.cash -= 1
            return True
        if self.dealer.is_bust():
            print(self.prompt(f'{self.player.__class__.__name__} wins!'))
            self.player.cash += 1
            return True
        return False

    def _win_score(self):
        if self.player.hand_value > self.dealer.hand_value:
            print(self.prompt(f'{self.player.__class__.__name__} wins!'))
            self.player.cash += 1
        elif self.dealer.hand_value > self.player.hand_value:
            print(self.prompt(f'{self.dealer.__class__.__name__} wins!'))
            self.player.cash -= 1
        else:
            print(self.prompt('It\'s a tie!'))

    def _reset_deck_and_hands(self):
        self.player.reset()
        self.dealer.reset()
        self.deck.reset()

    def _reading_pause_seconds(self, seconds):
        time.sleep(seconds)

    def _welcome_message(self):
        print(self.prompt('Welcome to Twenty-One!'))

    def _goodbye_message(self):
        print(self.prompt('Thanks for playing. Goodbye!'))

game = TwentyOne()
game.play()
