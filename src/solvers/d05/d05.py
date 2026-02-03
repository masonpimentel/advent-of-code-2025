"""Day 5"""

from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


class Day05(Day):
    """Cafeteria"""

    def get_pt_1(self, values: list[int], merged_ranges: list[tuple[int, int]]) -> int:
        res = 0

        len_merged_ranges = len(merged_ranges)

        for value in values:
            l = 0
            r = len_merged_ranges - 1

            while l < r:
                mid = l + ((r - l) // 2)

                if value < merged_ranges[mid][0]:
                    r = mid
                else:
                    l = mid + 1

            for check_idx in [l - 1, l, l + 1]:
                if (0 <= check_idx < len_merged_ranges) and (
                    merged_ranges[check_idx][0] <= value <= merged_ranges[check_idx][1]
                ):
                    res += 1
                    break

        return res

    def get_pt_2(self, merged_ranges: list[tuple[int, int]]) -> int:
        res = 0

        for merged_range in merged_ranges:
            left, right = merged_range[0], merged_range[1]

            res += right - left + 1

        return res

    def solve(self) -> SolveInfo:
        is_ranges = True

        ranges: list[tuple[int, int]] = []
        values: list[int] = []

        with open(get_path("05"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                if line == "\n":
                    is_ranges = False
                else:

                    if is_ranges:
                        left, right = line.split("-")
                        ranges.append((int(left), int(right)))
                    else:
                        values.append(int(line))

                line = f.readline()

        ranges.sort()
        values.sort()

        len_ranges = len(ranges)
        cur = 0

        merged_ranges: list[tuple[int, int]] = []

        while cur < len_ranges:
            runner = cur + 1
            new_left = ranges[cur][0]
            new_right = ranges[cur][1]

            while runner < len_ranges and new_right >= ranges[runner][0]:
                new_right = max(new_right, ranges[runner][1])
                cur += 1
                runner += 1

            cur += 1
            merged_ranges.append((new_left, new_right))

        return SolveInfo(
            str(self.get_pt_1(values, merged_ranges)), str(self.get_pt_2(merged_ranges))
        )
