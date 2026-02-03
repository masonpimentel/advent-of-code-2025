"""Day 1"""

from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


# pylint: disable=R0903
class Day01(Day):
    """Secret Entrance"""

    def solve(self) -> SolveInfo:
        pt_1_res = 0
        pt_2_res = 0
        pos = 50
        zero_clicks = 0

        with open(get_path("01"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                direc, val = line[0], int(line[1:])

                if pos == 0 and direc == "L":
                    needed = 100
                else:
                    needed = pos if direc == "L" else 100 - pos

                this_zero_clicks = 0

                moves = val
                if moves >= needed:
                    this_zero_clicks += 1
                    moves -= needed
                if moves > 0:
                    this_zero_clicks += moves // 100

                pos = (pos + (val if direc == "R" else -val)) % 100

                if pos == 0:
                    pt_1_res += 1
                    this_zero_clicks -= 1

                zero_clicks += this_zero_clicks

                line = f.readline()

        pt_2_res = pt_1_res + zero_clicks

        return SolveInfo(str(pt_1_res), str(pt_2_res))
