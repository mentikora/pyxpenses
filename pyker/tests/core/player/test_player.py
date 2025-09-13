from uuid import UUID

from app.core.card import Card, Rank, Suit
from app.core.player.player import Player


def test_player_initialization() -> None:
    player = Player("Alice")

    assert player.name == "Alice"
    assert isinstance(player.id, UUID)
    assert player.wallet.balance == 0
    assert player.hand.cards == []


def test_receive_card() -> None:
    player = Player("Bob")
    card = Card(Rank.ACE, Suit.SPADES)

    player.hand.receive_card(card)

    assert len(player.hand.cards) == 1
    assert player.hand.cards[0] == card


def test_drop_cards() -> None:
    player = Player("Charlie")
    card1 = Card(Rank.ACE, Suit.SPADES)
    card2 = Card(Rank.KING, Suit.HEARTS)

    player.hand.receive_card(card1)
    player.hand.receive_card(card2)
    assert len(player.hand.cards) == 2

    player.hand.drop_cards()
    assert player.hand.cards == []


def test_str_method() -> None:
    player = Player("David")
    result = str(player)

    assert player.name in result
    assert str(player.id) in result
