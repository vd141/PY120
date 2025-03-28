'''

'''

import random

class Card:
    '''
    card maps each rank to a numerical value for the min/max functions
    '''

    RANK_VALUE = {
        'Jack': 11,
        'Queen': 12,
        'King': 13,
        'Ace': 14,
    }
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = Card.RANK_VALUE.get(self.rank, self.rank)

    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

class Deck:
    '''
    shuffling can be simulated by drawing a random card
    '''
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
             
    def __init__(self):
        '''
        create a list of cards
        '''

        self._reset()
        
    def __str__(self):
        return str([str(card) for card in self._deck])
    
    def _reset(self):
        self._deck = [Card(rank, suit) 
                      for rank in Deck.RANKS
                      for suit in Deck.SUITS]
        random.shuffle(self._deck)

    def draw(self):
        if not self._deck:
            self.__init__()
        return self._deck.pop(0)
    
# Include Card and Deck classes from the last two exercises.

class PokerHand:

    ROYAL = {'Ace', 'King', 'Queen', 'Jack', 10}


    def __init__(self, deck):
        '''
        store hand in a list (pop deck 5 times)
        '''
        self._hand = [deck.draw() for _ in range(5)]
        self._suits = [card.suit for card in self._hand]
        self._ranks = [card.rank for card in self._hand]
        self._values = [card.value for card in self._hand]

    def print(self):
        print([str(hand) for hand in self._hand])
        # print([str(suit) for suit in self._suits])
        # print([str(rank) for rank in self._ranks])

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        '''
        all cards are from the same suit

        royal is A, K, Q, J, 10
        '''

        same_suit = len(set(self._suits)) == 1
        is_royal = set(self._ranks) == PokerHand.ROYAL

        return same_suit and is_royal

    def _is_straight_flush(self):
        '''
        five cards in a sequence, all in the same suit
        '''

        same_suit = len(set(self._suits)) == 1
        min_num = min(self._values)
        max_num = max(self._values)
        in_sequence = set(range(min_num, max_num + 1)) == set(self._values)
        
        return in_sequence and same_suit

    def _is_four_of_a_kind(self):
        '''
        all four cards of the same rank

        two ranks allowed in hand

        must count 4 of one rank (either)
        '''

        unique_ranks = set(self._ranks)

        if len(unique_ranks) == 2:
            list_unique_ranks = list(unique_ranks)
            return 4 in [self._ranks.count(list_unique_ranks[0]), 
                                self._ranks.count(list_unique_ranks[1])]
    
        return False

    def _is_full_house(self):
        '''
        three of a kind with a pair
        '''
        unique_ranks = set(self._ranks)

        if len(unique_ranks) == 2:
            list_unique_ranks = list(unique_ranks)
            return 3 in [self._ranks.count(list_unique_ranks[0]), 
                                self._ranks.count(list_unique_ranks[1])]
    
        return False

    def _is_flush(self):
        '''
        any five cards of the same suit, but not in a sequence
        '''

        return len(set(self._suits)) == 1

    def _is_straight(self):
        '''
        five cards in a sequence, but not of the same suit
        '''
        min_num = min(self._values)
        max_num = max(self._values)
        return set(range(min_num, max_num + 1)) == set(self._values)

    def _is_three_of_a_kind(self):
        '''
        three cards of the same rank (other 2 can be whatever)

        for each unique rank, return True if count is 3
        '''
        
        for rank in set(self._ranks):
            if self._ranks.count(rank) == 3:
                return True
        return False

    def _is_two_pair(self):
        '''
        two different pairs (5th card can be anything)

        get unique ranks

        for each unique rank, count occurrences
            if count is 3 or above, disqualify
            if count is 2, continue with next rank
        '''
        
        unique_ranks = set(self._ranks)
        doubles = 0

        for rank in unique_ranks:
            if self._ranks.count(rank) >= 3:
                return False
            if self._ranks.count(rank) == 2:
                doubles += 1
            if doubles == 2:
                return True
            
        return False

    def _is_pair(self):
        '''
        two cards of the same rank (other 3 can be anything)
        '''
        unique_ranks = set(self._ranks)

        for rank in unique_ranks:
            if self._ranks.count(rank) == 2:
                return True
            
        return False

# deck = Deck()
# hand = PokerHand(deck)

# hand.print()

hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand._suits)
print(hand._ranks)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")