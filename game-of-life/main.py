from rich.console import Console
import time
from board import create_board, render_board, analyze_board
from cell import cell_functions


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
