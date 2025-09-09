from core.table import Table
from core.player import Player


def main():
    me = Player(name="Dota2")
    you = Player(name="Dota3")
    him = Player(name="Dota4")
    table = Table()
    table.add_player(me)
    table.add_player(you)
    table.add_player(him)
    table.give_cards()
    table._debugger_info()


if __name__ == "__main__":
    main()
