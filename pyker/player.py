import uuid
from card import Card


class Player:
    def __init__(self, name: str):
        self._cards: list[Card] = []
        self.id: uuid.UUID = uuid.uuid4()
        self.name: str = name

    def receive_card(self, card: Card):
        self._cards.append(card)

    def drop_cards(self):
        self._cards.clear()

    def __str__(self):
        return f"{self.name} {self.id}"

    @property
    def cards(self):
        return self._cards
