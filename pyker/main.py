from app.core.table import Table
from app.core.player import Player

# from app.games.blackjack.blackjack import card_value, summarize_hand

from itertools import chain


def main():
    me = Player(name="Dota1")
    you = Player(name="Dota2")
    him = Player(name="Dota3")
    table = Table()
    table.add_player(me)
    # table.add_player(you)
    # table.add_player(him)
    table.give_cards()

    print(me.id)
    # cards_value = summarize_hand(
    #     [card_value(card) for card in chain.from_iterable(me.cards)]
    # )
    # print(cards_value)
    # table._debugger_info()


if __name__ == "__main__":
    main()
