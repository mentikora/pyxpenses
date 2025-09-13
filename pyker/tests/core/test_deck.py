from itertools import product

from app.core.card import Card, Rank, Suit
from app.core.deck import Deck


def test_deck_creation() -> None:
    deck = Deck()

    assert len(deck.deck) == 52

    # Check all unique cards
    all_combinations = set((rank, suit) for rank, suit in product(Rank, Suit))
    deck_combinations = set((card.rank, card.suit) for card in deck.deck)

    assert deck_combinations == all_combinations


def test_deck_shuffle_changes_order() -> None:
    deck1 = Deck()
    deck2 = Deck()

    assert deck1.deck != deck2.deck or id(deck1.deck) != id(deck2.deck)


def test_draw_cards() -> None:
    deck = Deck()
    initial_count = len(deck.deck)
    drawn = deck.draw(3)

    assert len(drawn) == 3
    assert len(deck.deck) == initial_count - 3
    for card in drawn:
        assert isinstance(card, Card)


def test_draw_too_many_raises() -> None:
    deck = Deck()

    try:
        deck.draw(53)
        assert False, "Expected ValueError when drawing too many cards"
    except ValueError as e:
        assert str(e) == "No cards left"


def test_reset_deck() -> None:
    deck = Deck()
    deck.draw(10)

    assert len(deck.deck) == 42

    deck.reset()

    assert len(deck.deck) == 52
