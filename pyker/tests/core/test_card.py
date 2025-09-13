import pytest
from app.core.card import Card, Rank, Suit


def test_card_initialization() -> None:
    card = Card(rank=Rank.ACE, suit=Suit.CLUBS)

    assert card.rank == Rank.ACE
    assert card.suit == Suit.CLUBS


def test_rank_values() -> None:
    assert Rank.TWO.value == 2
    assert Rank.ACE.value == 14
    assert Rank.JACK.value == 11


def test_suit_values() -> None:
    assert Suit.SPADES.value == "♠"
    assert Suit.HEARTS.value == "♥"
    assert Suit.DIAMONDS.value == "♦"
    assert Suit.CLUBS.value == "♣"


def test_card_numeric_repr():
    card = Card(Rank.FIVE, Suit.SPADES)
    assert card.repr() == "5♠"


@pytest.mark.parametrize(
    "rank,expected",
    [
        (Rank.JACK, "JACK♥"),
        (Rank.QUEEN, "QUEEN♥"),
        (Rank.KING, "KING♥"),
        (Rank.ACE, "ACE♥"),
    ],
)
def test_card_face_repr(rank, expected):
    card = Card(rank, Suit.HEARTS)

    assert card.repr() == expected


def test_card_is_immutable():
    card = Card(Rank.TWO, Suit.CLUBS)
    with pytest.raises(AttributeError):
        card.rank = Rank.THREE
    with pytest.raises(AttributeError):
        card.suit = Suit.SPADES
