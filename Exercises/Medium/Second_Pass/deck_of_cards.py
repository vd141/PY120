'''
deck of cards
'''
import random

class Card:
    VALUES = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    @property
    def value(self):
        return Card.VALUES.get(self.rank, self.rank)

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

class Deck:
    '''
    provides a draw method to deal one card. the deck should be shuffled
    when it is initialized. if no more cards remain when draw is called, the method
    should generate a new set of 52 shuffled cards, then deal one card from the
    new cards
    '''
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    
    def __init__(self):
        self._reset()

    def _reset(self):
        self._deck = [Card(rank, suit) 
                      for rank in Deck.RANKS
                      for suit in Deck.SUITS]
        random.shuffle(self._deck)
        
    def draw(self):
        if len(self._deck) == 0:
            self._reset()

        return self._deck.pop()


'''
test cases
'''
deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).