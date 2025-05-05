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
import copy
import time
import os

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
        values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
        card_names = [f'{face_name} of {suit}' for suit in Deck.SUITS
                                        for face_name in Deck.FACES]
        self._deck = [Card(name, values[index]) for index, name in enumerate(
            card_names)]
        random.shuffle(self._deck)
        
    def __str__(self):
        return str(list(str(card) for card in self._deck))

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
    def __init__(self):
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
        card_value = card.value
        if not self.has_ace and card_value is 'Ace':
            self.has_ace = True
            card_value = 11
        elif card_value is 'Ace':
            card_value = 1
        self.hand.append(card)
        self.hand_value += card_value

    def hit(self, card):
        print(self.prompt(f'{self.__class__.__name__} hits!'))
        self.add_to_hand(card)

    def stay(self):
        print(self.prompt(f'{self.__class__.__name__} stays!'))

class Dealer(Opponent):
    '''
    dealer has a strategy method, which dictates whether the dealer will hit or
    stay

    has a method to display one card
    '''
    def strategy(self, deck):
        if self.value < 17:
            self.hit(deck.draw())
        else:
            self.stay()

class Player(Opponent):
    '''
    player has a strategy method, which takes player input (hit or stay)

    player also has a cash attribute, which is initialized to 5
    '''
    pass

class TwentyOne:
    '''
    initializes deck and players. dictates game flow. decides a winner

    welcome message

    initialize deck and players

    deal cards to dealer and player

    prompt player for decision

    goodbye message

    '''
    pass