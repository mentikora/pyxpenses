from deck import Deck
from player import Player


def main():
    deck = Deck()
    player = Player(name="Player 1")

    print(len(deck.deck))
    print(deck.draw())
    print(deck.draw(2))
    print(len(deck.deck))


if __name__ == "__main__":
    main()
