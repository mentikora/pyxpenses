from ..card import Card


class Hand:
    """
    Represents Player's cards & actions
    """

    def __init__(self):
        self._cards: list[Card] = []

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

    @property
    def cards(self):
        """
        Return player's cards
        """
        return self._cards
