"""Day 11"""

from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


class Day11(Day):
    """Reactor"""

    def __init__(self) -> None:
        self.dp: dict[str, int] = {}
        self.graph: dict[str, list[str]] = {}

    def rec(self, cur: str, dac: bool, fft: bool) -> int:
        k = str((cur, dac, fft))

        if k in self.dp:
            return self.dp[k]

        if cur == "out" and dac and fft:
            return 1

        res = 0
        if cur in self.graph:
            for neigh in self.graph[cur]:
                res += self.rec(neigh, dac or cur == "dac", fft or cur == "fft")

        self.dp[k] = res
        return res

    def solve(self) -> SolveInfo:
        with open(get_path("11"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                parts = line.split(" ")

                src = parts[0][:-1]
                self.graph[src] = parts[1:]
                last = self.graph[src][-1]
                self.graph[src][-1] = last[:-1] if last[-1] == "\n" else last

                line = f.readline()

        pt_1_res = self.rec("you", True, True)
        self.dp = {}
        pt_2_res = self.rec("svr", False, False)

        return SolveInfo(str(pt_1_res), str(pt_2_res))
