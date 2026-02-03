"""Helper functions"""

from typing import TextIO, NamedTuple
from os.path import join


class GridInfo(NamedTuple):
    """Common components needed for grids"""

    grid: list[list[str]]
    rows: int
    cols: int


def get_grid(f: TextIO) -> GridInfo:
    line = f.readline()

    grid: list[list[str]] = []

    while line:
        row = list(line)
        grid.append(row[:-1] if row[-1] == "\n" else row)
        line = f.readline()

    return GridInfo(grid, len(grid), len(grid[0]))


def get_path(day: str) -> str:
    return join("src", "solvers", f"d{day}", "input.txt")


def check_row_and_col(row: int, col: int, rows: int, cols: int) -> bool:
    return row < 0 or row >= rows or col < 0 or col >= cols
