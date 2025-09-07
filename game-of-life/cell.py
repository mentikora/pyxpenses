from random import randint
from dataclasses import dataclass
from collections.abc import Callable
from functools import cache
from typing import List


@dataclass
class CellFunctions:
    """
    Container for Game of Life cell functions.

    Attributes:
        dead (Callable[[], int]): Function returning 0, representing a dead cell.
        alive (Callable[[], int]): Function returning 1, representing a live cell.
        dead_or_alive (Callable[[], int]): Function returning either 0 or 1 randomly.
    """

    dead: Callable[[], int]
    alive: Callable[[], int]
    dead_or_alive: Callable[[], int]
    is_dead: Callable[[int], bool]
    is_alive: Callable[[int], bool]


def cell_functions() -> CellFunctions:
    """
    Creates and returns a set of cell state functions for the Game of Life.

    Returns:
        CellFunctions: Dataclass containing:
            - dead: Returns 0 (dead cell)
            - alive: Returns 1 (alive cell)
            - dead_or_alive: Randomly returns 0 or 1 (dead or alive)
            - is_alive: Returns bool
            - is_dead: Returns bool
    """
    DEAD = 0
    ALIVE = 1

    @cache
    def dead() -> int:
        """Return the dead state of a cell (0)."""
        return DEAD

    def is_dead(x: int) -> bool:
        return x == DEAD

    @cache
    def alive() -> int:
        """Return the alive state of a cell (1)."""
        return ALIVE

    def is_alive(x: int) -> bool:
        return x == ALIVE

    def dead_or_alive(random_func=randint) -> int:
        """
        Return a random cell state: dead (0) or alive (1).

        Args:
            random_func (Callable[[int, int], int], optional):
                Random function to decide state. Defaults to `randint(0, 1)`.

        Returns:
            int: 0 if dead, 1 if alive
        """
        return alive() if random_func(0, 1) else dead()

    return CellFunctions(
        dead=dead,
        alive=alive,
        dead_or_alive=dead_or_alive,
        is_dead=is_dead,
        is_alive=is_alive,
    )


def calc_cell_state(board: List[List[int]], x: int, y: int):
    rows = len(board)
    cols = len(board[0])
    neighbors = 0
    # fmt: off
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    # fmt: on

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= ny < rows and 0 <= nx < cols:
            neighbors += board[ny][nx]

    return board[y][x], neighbors
