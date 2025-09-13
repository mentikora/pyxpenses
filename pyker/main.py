from app.games.blackjack.blackjack import BlackjackTable

from pyker.app.core.player.player import Player


def main():
    me = Player(name="Dota1")

    blackjack = BlackjackTable()
    blackjack.add_player(me)
    blackjack.give_cards()

    blackjack.initial_deal()
    blackjack._debugger_info()


if __name__ == "__main__":
    main()
