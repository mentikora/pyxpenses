from dataclasses import dataclass
from enum import Enum


class Rank(Enum):
    """
    Card rank with value
    """

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Suit(Enum):
    """
    Card suit with symbol
    """

    SPADES = "♠"
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"


@dataclass(frozen=True)
class Card:
    """
    Represents a general playing card
    """

    rank: Rank
    suit: Suit

    def repr(self) -> str:
        """
        Visual card representation
        """
        match self.rank:
            case Rank.JACK | Rank.QUEEN | Rank.KING | Rank.ACE:
                return f"{self.rank.name}{self.suit.value}"
            case _:
                return f"{self.rank.value}{self.suit.value}"
