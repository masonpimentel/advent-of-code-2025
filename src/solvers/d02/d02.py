"""Day 2"""

from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


class Day02(Day):
    """Gift Shop"""

    def is_repeat_twice(self, num: str) -> bool:
        l_num = len(num)

        if l_num % 2 != 0:
            return False

        half = l_num // 2
        return num[:half] == num[half:]

    def is_repeat(self, num: str) -> bool:
        s_num = str(num)
        l_num = len(num)

        for width in range(1, (l_num // 2) + 1):
            if l_num % width != 0:
                continue

            found = True
            for i in range(1, (l_num // width)):
                if s_num[i * width : (i + 1) * width] != s_num[:width]:
                    found = False
                    break

            if found:
                return True

        return False

    def solve(self) -> SolveInfo:
        pt_1_res = 0
        pt_2_res = 0

        with open(get_path("02"), encoding="utf-8") as f:
            line = f.readline()

            for r in line.split(","):
                s = r.split("-")
                start, end = int(s[0]), int(s[1])

                for v in range(start, end + 1):
                    if self.is_repeat_twice(str(v)):
                        pt_1_res += v
                    if self.is_repeat(str(v)):
                        pt_2_res += v

        return SolveInfo(str(pt_1_res), str(pt_2_res))
