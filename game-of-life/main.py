import time

from board import analyze_board, create_board, render_board
from cell import cell_functions
from rich.console import Console


def run():
    console = Console()
    cell = cell_functions()
    board = create_board(width=100, height=40, cell=cell.dead_or_alive)

    while True:
        console.clear()
        render_board(board)
        board = analyze_board(board=board)
        time.sleep(0.09)


def main():
    run()


if __name__ == "__main__":
    main()
