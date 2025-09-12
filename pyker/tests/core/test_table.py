from app.core.table import Table
from app.core.deck import Deck
from app.core.player import Player


def test_table_initialization():
    table = Table()

    assert isinstance(table.players, list)
    assert isinstance(table.deck, Deck)
    assert len(table.players) == 0
    assert table.deck is not None
    assert table.id is not None


def test_add_player():
    table = Table()
    player = Player("Alice")
    table.add_player(player)

    assert len(table.players) == 1
    assert table.players[0] == player


def test_add_same_player_raises():
    table = Table()
    player = Player("Bob")
    table.add_player(player)

    try:
        table.add_player(player)
        assert False, "Expected ValueError when adding the same player"
    except ValueError as e:
        assert str(e) == f"{player.name} is already playing"


def test_remove_player():
    table = Table()
    player1 = Player("Alice")
    player2 = Player("Bob")
    table.add_player(player1)
    table.add_player(player2)
    table.remove_player(player1.id)

    assert len(table.players) == 1
    assert table.players[0] == player2


def test_give_cards():
    table = Table()
    player1 = Player("Alice")
    player2 = Player("Bob")
    table.add_player(player1)
    table.add_player(player2)

    initial_deck_size = len(table.deck.deck)
    table.give_cards(2)

    assert len(player1.cards) == 2
    assert len(player2.cards) == 2
    assert len(table.deck.deck) == initial_deck_size - 4


def test_give_cards_with_deck_exhausted():
    table = Table()
    player = Player("Alice")
    table.add_player(player)

    for _ in range(26):
        table.give_cards(2)
    try:
        table.give_cards(1)
        assert False, "Expected ValueError when deck is empty"
    except ValueError:
        pass
