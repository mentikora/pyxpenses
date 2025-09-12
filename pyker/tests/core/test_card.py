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


def test_card_str() -> None:
    card = Card(Rank.QUEEN, Suit.HEARTS)

    assert str(card) == f"{Rank.QUEEN.value}{Suit.HEARTS.value}"
