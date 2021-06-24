# Design a class deck of cards that can be used for different card game
# applications.

# What is the deck of cards: A "standard" deck of playing cards consists of 52 Cards
# in each of the 4 suits of Spades, Hearts, Diamonds, and Clubs. Each suit contains
#  13 cards: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King.

from random import shuffle


class Deck:
    def __init__(self):
        """ build the deck of cards afresh when object is initialized."""
        suits = ["hearts", "spade", "diamond", "clubs"]
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append((value, suit))

    def count(self):
        """ Get count of cards in the deck."""
        return(len(self.cards))

    def shuffle(self):
        """ Shuffle the deck if num of cards left is atleast 2 """
        if self.count() > 1:
            print("Shuffling the deck!")
            shuffle(self.cards)
        return self

    def _deal(self, num):
        """Deal specified number of cards from the top of the deck"""
        current_count = self.count()
        if current_count == 0:
            raise ValueError("Deck is empty, all cards have been dealt.")
        if num == 0:
            raise ValueError("Number of cards to deal cannot be zero !")
# if the num asked for is greater than what is in the deck then deal the
# minimum of the 2.
        actual_num_cards = min(current_count, num)
        print(f"Number cards that will be dealt is {actual_num_cards}")
        cards_dealt = self.cards[-actual_num_cards:]
        self.cards = self.cards[:-actual_num_cards]
        if self.cards == 0:
            print("Last few cards have been dealt!")

        return cards_dealt

    def deal_card(self):
        """Deal a single card from the top of the deck."""
        return self._deal(1)[0]

    def deal_hand(self, num):
        """Deal a hand of the specified number of cards."""
# check if invald hand size and raise exception.
        if num <= 0:
            raise ValueError(
                f"invalid value {num} for number of cards to deal.")
        return self._deal(num)


deck = Deck()
print(len(deck.cards))  # check num of cards in the deck.

draw1 = deck.deal_card()
print(draw1)  # print which card has been dealt.

hand1 = deck.deal_hand(3)
print(hand1)  # print which 3 cards have been dealt.

deck.shuffle()

hand2 = deck.deal_hand(3)
print(hand2)

print(len(deck.cards))
