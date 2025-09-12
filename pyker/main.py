from app.core.player import Player

from app.games.blackjack.blackjack import BlackjackTable


def main():
    me = Player(name="Dota1")

    blackjack = BlackjackTable()
    blackjack.add_player(me)

    # blackjack.initial_deal()
    blackjack._debugger_info()


if __name__ == "__main__":
    main()
