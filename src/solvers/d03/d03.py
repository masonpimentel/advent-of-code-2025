"""Day 3"""

from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path, get_grid


# pylint: disable=R0903
class Day03(Day):
    """Lobby"""

    def process_battery(self, battery: list[str], joltages: int) -> int:
        len_battery_plus_one = len(battery) + 1
        answer = ""

        start = 0
        for end in range(len_battery_plus_one - joltages, len_battery_plus_one):
            best = max(battery[start:end])

            start = battery.index(best, start) + 1

            answer += best

        return int(answer)

    def solve(self) -> SolveInfo:
        pt_1_res = 0
        pt_2_res = 0

        mat: list[list[str]] = []

        with open(get_path("03"), encoding="utf-8") as f:
            mat, _, __ = get_grid(f)

        for row in mat:
            pt_1_res += self.process_battery(row, 2)
            pt_2_res += self.process_battery(row, 12)

        return SolveInfo(str(pt_1_res), str(pt_2_res))
