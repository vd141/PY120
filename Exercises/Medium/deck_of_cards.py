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

        self._deck = [Card(rank, suit) 
                      for rank in Deck.RANKS
                      for suit in Deck.SUITS]
        random.shuffle(self._deck)
        
    def __str__(self):
        return str([str(card) for card in self._deck])

    def draw(self):
        if not self._deck:
            self.__init__()
        return self._deck.pop(0)

deck = Deck()
print(deck)
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