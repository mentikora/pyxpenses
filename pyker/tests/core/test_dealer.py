from app.core.dealer import Dealer
from app.core.player.player import Player


def test_dealer_is_player():
    dealer = Dealer()

    assert isinstance(dealer, Player)


def test_dealer_default_name():
    dealer = Dealer()

    assert dealer.name == "Blackjack Dealer"


def test_dealer_custom_name():
    dealer = Dealer(name="John")

    assert dealer.name == "John"


def test_dealer_inherits_player_methods():
    dealer = Dealer()

    assert hasattr(dealer, "hand")
    assert hasattr(dealer, "wallet")
