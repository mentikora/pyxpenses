import random
from card import Card, Rank, Suit
from itertools import product


class Deck:
    def __init__(self):
        self.deck = []
        self._create()
        self.shuffle()

    def _create(self):
        self.deck = []
        card_posibilities = product(Rank, Suit)

        for rank, suit in card_posibilities:
            card = Card(rank=rank, suit=suit)
            self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def reset(self):
        self._create()

    def draw(self, amount: int = 1) -> Card:
        if len(self.deck) < amount:
            raise ValueError("No cards left")

        return [self.deck.pop() for _ in range(amount)]
