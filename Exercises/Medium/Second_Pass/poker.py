'''

'''
from deck_of_cards import Card, Deck

# Include Card and Deck classes from the last two exercises.

class PokerHand:
    def __init__(self, deck):
        '''
        pop 5 cards from deck and save them to hand
        '''
        self._hand = [deck.draw() for _ in range(5)]
        self._hand_ranks = [card.value for card in self._hand]
        self._hand_suits = [card.suit for card in self._hand]
        self._unique_rank = set(self._hand_ranks)
        self._unique_suit = set(self._hand_suits)

    def print(self):
       for card in self._hand:
           print(card)

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
        A, K, Q, J, 10 all the same suit
        '''
        pass

    def _is_straight_flush(self):
        '''
        five cards in a sequence, all in the same suit
        '''
        pass

    def _is_four_of_a_kind(self):
        '''
        all four cards of the same rank
        '''
        pass

    def _is_full_house(self):
        '''
        three of a kind with a pair
        '''
        pass

    def _is_flush(self):
        '''
        any five cards of the same suit, but not in a sequence
        '''
        pass

    def _is_straight(self):
        '''
        five cards in a sequence, but not of the same suit
        '''
        if len(self._unique_rank) == 5:
            smallest = min(self._hand_ranks)
            golden_sequence = range(smallest, smallest + 6)
            return True if list(sorted(self._hand_ranks)) == golden_sequence else False
        

    def _is_three_of_a_kind(self):
        '''
        three cards of the same rank
        '''
        for rank in self._unique_rank:
            if self._hand_ranks.count(rank) == 3:
                return True
            
        return False

    def _is_two_pair(self):
        '''
        two different pairs
        '''
        pass

    def _is_pair(self):
        '''
        two cards of the same rank

        for unique cards, return True if count for any rank is True
        '''
        for rank in self._unique_rank:
            if self._hand_ranks.count(rank) == 2:
                return True
            
        return False



'''
testing a class
'''

hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

# hand = PokerHand(
#     TestDeck(
#         [
#             Card("Ace", "Hearts"),
#             Card("Queen", "Hearts"),
#             Card("King", "Hearts"),
#             Card("Jack", "Hearts"),
#             Card(10, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Royal flush")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(8, "Clubs"),
#             Card(9, "Clubs"),
#             Card("Queen", "Clubs"),
#             Card(10, "Clubs"),
#             Card("Jack", "Clubs"),
#         ]
#     )
# )
# print(hand.evaluate() == "Straight flush")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(3, "Hearts"),
#             Card(3, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(3, "Spades"),
#             Card(3, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "Four of a kind")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(3, "Hearts"),
#             Card(3, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(3, "Spades"),
#             Card(5, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Full house")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(10, "Hearts"),
#             Card("Ace", "Hearts"),
#             Card(2, "Hearts"),
#             Card("King", "Hearts"),
#             Card(3, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Flush")

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

# hand = PokerHand(
#     TestDeck(
#         [
#             Card("Queen", "Clubs"),
#             Card("King", "Diamonds"),
#             Card(10, "Clubs"),
#             Card("Ace", "Hearts"),
#             Card("Jack", "Clubs"),
#         ]
#     )
# )
# print(hand.evaluate() == "Straight")

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

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(9, "Hearts"),
#             Card(9, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(8, "Spades"),
#             Card(5, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Two pair")

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

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(2, "Hearts"),
#             Card("King", "Clubs"),
#             Card(5, "Diamonds"),
#             Card(9, "Spades"),
#             Card(3, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "High card")