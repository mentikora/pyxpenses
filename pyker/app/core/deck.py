import random
from itertools import product

from .card import Card, Rank, Suit
from ..utils.id import new_id


class Deck:
    """
    Standard 52-card deck
    """

    def __init__(self):
        self.deck = []
        self.id = new_id()
        self._create()
        self.shuffle()

    def _create(self):
        """
        Create a 52-card deck
        """
        self.deck = []
        card_posibilities = product(Rank, Suit)

        for rank, suit in card_posibilities:
            card = Card(rank=rank, suit=suit)
            self.deck.append(card)

    def shuffle(self):
        """
        Randomly shuffle the deck
        """
        random.shuffle(self.deck)

    def reset(self):
        """
        Reset the deck to a full, shuffled state
        """
        self._create()

    def draw(self, amount: int = 1) -> Card:
        """
        Return the top card/s from the deck
        """
        if len(self.deck) < amount:
            raise ValueError("No cards left")

        return [self.deck.pop() for _ in range(amount)]
