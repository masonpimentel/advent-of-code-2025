"""Day 4"""

from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_grid, get_path


class Day04(Day):
    """Printing Department"""

    def __init__(self) -> None:
        self.mat: list[list[str]] = []
        self.rows = 0
        self.cols = 0

    def process_top_row(self, mat: list[list[str]], row: int, col: int) -> int:
        adjs = 0

        # top left
        if row > 0 and col > 0 and mat[row - 1][col - 1] == "@":
            adjs += 1
        # top
        if row > 0 and mat[row - 1][col] == "@":
            adjs += 1
        # top right
        if row > 0 and col < self.cols - 1 and mat[row - 1][col + 1] == "@":
            adjs += 1
        # left
        if col > 0 and mat[row][col - 1] == "@":
            adjs += 1

        return adjs

    def can_access(self, mat: list[list[str]], row: int, col: int) -> bool:
        adjs = self.process_top_row(mat, row, col)

        if adjs > 3:
            return False

        # right
        if col < self.cols - 1 and mat[row][col + 1] == "@":
            adjs += 1

        if adjs > 3:
            return False

        # bottom left
        if row < self.rows - 1 and col > 0 and mat[row + 1][col - 1] == "@":
            adjs += 1

        if adjs > 3:
            return False

        # bottom
        if row < self.rows - 1 and mat[row + 1][col] == "@":
            adjs += 1

        if adjs > 3:
            return False

        # bottom right
        if row < self.rows - 1 and col < self.cols - 1 and mat[row + 1][col + 1] == "@":
            adjs += 1

        if adjs > 3:
            return False

        return True

    def iterate(self, mat: list[list[str]]) -> int:
        res = 0

        rows = len(mat)
        cols = len(mat[0])

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] != "@":
                    continue

                if self.can_access(mat, row, col):
                    res += 1

                    mat[row][col] = "x"

        return res

    def solve(self) -> SolveInfo:
        pt_1_res = 0
        pt_2_res = 0

        with open(get_path("04"), encoding="utf-8") as f:
            self.mat, self.rows, self.cols = get_grid(f)

        for row in range(self.rows):
            for col in range(self.cols):
                if self.mat[row][col] != "@":
                    continue

                if self.can_access(self.mat, row, col):
                    pt_1_res += 1

        mat = [list(row) for row in self.mat]
        while True:
            this_res = self.iterate(mat)

            if this_res == 0:
                break

            pt_2_res += this_res

        return SolveInfo(str(pt_1_res), str(pt_2_res))
