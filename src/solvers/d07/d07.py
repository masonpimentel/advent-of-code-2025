"""Day 7"""

from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path, get_grid


class Day07(Day):
    """Laboratories"""

    def __init__(self) -> None:
        self.graph: list[list[str]] = []
        self.dp: dict[int, dict[int, int]] = {}

    def rec(self, row: int, col: int, tot_rows: int) -> int:
        if row >= tot_rows:
            return 1

        if row in self.dp:
            if col in self.dp[row]:
                return self.dp[row][col]
        else:
            self.dp[row] = {}

        if row % 2 == 1:
            return self.rec(row + 1, col, tot_rows)

        if self.graph[row][col] == "^":
            res = self.rec(row + 1, col - 1, tot_rows) + self.rec(
                row + 1, col + 1, tot_rows
            )
        else:
            res = self.rec(row + 1, col, tot_rows)

        self.dp[row][col] = res

        return res

    def solve(self) -> SolveInfo:
        beams: set[int] = set()
        start_col = -1
        pt_1_res = 0

        with open(get_path("07"), encoding="utf-8") as f:
            line = f.readline()

            for i, c in enumerate(line):
                if c == "S":
                    beams.add(i)
                    start_col = i
                    break

            line = f.readline()

            skip = True
            while line:
                if skip:
                    skip = False
                else:
                    for i, c in enumerate(line):
                        if c == "^" and (i in beams):
                            beams.remove(i)
                            beams.add(i - 1)
                            beams.add(i + 1)
                            pt_1_res += 1

                    skip = True

                line = f.readline()

        with open(get_path("07"), encoding="utf-8") as f:
            self.graph, rows, _ = get_grid(f)

        for i, c in enumerate(self.graph[0]):
            if c == "S":
                start_col = i
                break

        return SolveInfo(str(pt_1_res), str(self.rec(1, start_col, rows)))
