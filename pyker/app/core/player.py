from ..utils.id import new_id
from .card import Card


class Player:
    """
    Represents a player at the table
    """

    def __init__(self, name: str):
        self._cards: list[Card] = []
        self.id = new_id()
        self.name: str = name
        self.money: int = 0

    def receive_card(self, card: Card):
        """
        Add a card to the player's hand
        """
        self._cards.append(card)

    def drop_cards(self):
        """
        Cleanup player's hand
        """
        self._cards.clear()

    def __str__(self):
        return f"{self.name} {self.id}"

    @property
    def cards(self):
        """
        Return player's cards
        """
        return self._cards
