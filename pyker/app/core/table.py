import uuid

from ..utils.id import new_id
from .deck import Deck
from .player import Player


class Table:
    def __init__(self):
        self.players: list[Player] = []
        self.deck = Deck()
        self.id = new_id()

    def add_player(self, new_player: Player):
        for player in self.players:
            if player.id == new_player.id:
                raise ValueError(f"{player.name} is already playing")

        self.players.append(new_player)

    def remove_player(self, id: uuid.UUID):
        self.players = [player for player in self.players if player.id != id]

    def reset(self):
        pass

    def give_cards(self, amount: int = 2):
        for player in self.players:
            for _ in range(amount):
                card = self.deck.draw()
                player.receive_card(card)

    def _debugger_info(self):
        print("==========")
        print("Deck:")
        print(self.deck.deck)
        print("Players:")
        for player in self.players:
            print(player)
