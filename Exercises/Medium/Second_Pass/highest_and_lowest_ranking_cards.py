class Card:
    '''
    further exploration:

    given all equal card ranks, Spades > Hearts > Clubs > Diamonds

    give spades a value of 400
    hearts = 300
    clubs = 200
    diamonds = 100
    
    '''
    VALUES = {
        'Jack': 11,
        'Queen': 12,
        'King': 13,
        'Ace': 14,
    }

    SUITS = {
        'Spades': 400,
        'Hearts': 300,
        'Clubs': 200,
        'Diamonds': 100,
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = Card.VALUES.get(rank, rank)

    def __lt__(self, other):
        if isinstance(other, Card):
            if self.value == other.value:
                self._adjusted_value = Card.SUITS.get(self.suit) + self.value
                other._adjusted_value = Card.SUITS.get(other.suit) + self.value
                return self._adjusted_value < other._adjusted_value
            return self.value < other.value
        
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Card):
            if self.value == other.value:
                self._adjusted_value = Card.SUITS.get(self.suit) + self.value
                other._adjusted_value = Card.SUITS.get(other.suit) + self.value
                return self._adjusted_value > other._adjusted_value
        return self.value > other.value
        
        return NotImplemented
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return (self.value, self.rank) == (other.value, other.rank)
        
        return NotImplemented


cards = [Card(2, 'Hearts'),
         Card(10, 'Diamonds'),
         Card('Ace', 'Clubs')]
print(min(cards) == Card(2, 'Hearts'))             # True
print(max(cards) == Card('Ace', 'Clubs'))          # True
print(str(min(cards)) == "2 of Hearts")            # True
print(str(max(cards)) == "Ace of Clubs")           # True

cards = [Card(5, 'Hearts')]
print(min(cards) == Card(5, 'Hearts'))             # True
print(max(cards) == Card(5, 'Hearts'))             # True
print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

cards = [Card(4, 'Hearts'),
         Card(4, 'Diamonds'),
         Card(10, 'Clubs')]
print(min(cards).rank == 4)                        # True
print(max(cards) == Card(10, 'Clubs'))             # True
print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

cards = [Card(7, 'Diamonds'),
         Card('Jack', 'Diamonds'),
         Card('Jack', 'Spades')]
print(min(cards) == Card(7, 'Diamonds'))           # True
print(max(cards).rank == 'Jack')                   # True
print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

cards = [Card(8, 'Diamonds'),
         Card(8, 'Clubs'),
         Card(8, 'Spades')]
print(min(cards).rank == 8)                        # True
print(max(cards).rank == 8)                        # True
print(min(cards).suit == 'Diamonds')
print(min(cards).suit)
print(cards[0]._adjusted_value)
print(cards[1]._adjusted_value)
print(cards[2]._adjusted_value)
cards.sort()
print([str(card) for card in cards])