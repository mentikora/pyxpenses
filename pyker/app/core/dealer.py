from .player import Player


class Dealer(Player):
    """
    Subclass of Player,
    represents the dealer
    """

    def __init__(self, name: str = "Blackjack Dealer"):
        super().__init__(name=name)
