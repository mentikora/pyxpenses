from ...utils.id import new_id
from .hand import Hand
from .wallet import Wallet


class Player:
    """
    Represents a player at the table
    """

    def __init__(self, name: str, initial_money: int = 0):
        self.name: str = name
        self.id = new_id()
        self.hand = Hand()
        self.wallet = Wallet(initial_money)

    def __str__(self):
        return f"{self.name} {self.id}"
