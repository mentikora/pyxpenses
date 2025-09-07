from collections.abc import Callable
from typing import List
from rich import print
from cell import calc_cell_state, cell_functions


def create_board(
    *, width: int, height: int, cell: Callable[[], int]
) -> List[List[int]]:
    return [[cell() for _ in range(width)] for _ in range(height)]


def render_board(board: List[List[int]]) -> None:
    """Return an ASCII representation of the board."""
    height = len(board)
    width = len(board[0]) if height > 0 else 0

    def cell_repr(v: int) -> str:
        return "*" if v == 1 else "-"

    lines = ["-" * (width + 2)]

    for row in board:
        line = "|" + "".join(cell_repr(v) for v in row) + "|"
        lines.append(line)

    lines.append("-" * (width + 2))

    print("\n".join(lines))


def analyze_board(board):
    width = len(board[0])
    height = len(board)
    cell = cell_functions()
    dead_board = create_board(width=width, height=height, cell=cell.dead)

    for i in range(width):
        for j in range(height):
            current, neighbor_weight = calc_cell_state(board, i, j)

            if cell.is_alive(current):
                # 0 or 1 - dead
                # 3+ - dead
                if (
                    neighbor_weight == 0 or neighbor_weight == 1
                ) or neighbor_weight > 3:
                    dead_board[j][i] = cell.dead()
                # 2 or 3 - alive
                if neighbor_weight == 2 or neighbor_weight == 3:
                    dead_board[j][i] = cell.alive()
            if cell.is_dead(current):
                if neighbor_weight == 3:
                    dead_board[j][i] = cell.alive()
                else:
                    dead_board[j][i] = cell.dead()

    return dead_board
