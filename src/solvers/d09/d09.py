"""Day 9"""

from typing import NamedTuple
from math import sqrt
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


# pylint: disable=C0115
class Rectangle(NamedTuple):
    size: int
    src_x: int
    src_y: int
    dst_x: int
    dst_y: int


# pylint: disable=C0115
class Line(NamedTuple):
    length: float
    src_x: int
    src_y: int
    dst_x: int
    dst_y: int


class Day09(Day):
    """Movie Theatre"""

    def get_pt_1(self, x_y: list[tuple[int, int]]) -> int:
        len_x_y = len(x_y)
        res = 0

        for i in range(len_x_y):
            for j in range(i + 1, len_x_y):
                src = x_y[i]
                dst = x_y[j]

                size = (abs(src[0] - dst[0]) + 1) * (abs(src[1] - dst[1]) + 1)
                res = max(res, size)

        return res

    def get_rects(self, x_y: list[tuple[int, int]]) -> list[Rectangle]:
        rects: list[Rectangle] = []
        len_x_y = len(x_y)

        for i in range(len_x_y):
            for j in range(i + 1, len_x_y):
                src = x_y[i]
                dst = x_y[j]

                src_x, src_y = src[0], src[1]
                dst_x, dst_y = dst[0], dst[1]

                rects.append(
                    Rectangle(
                        abs(dst_y - src_y) * abs(dst_x - src_x),
                        src_x,
                        src_y,
                        dst_x,
                        dst_y,
                    )
                )

        return sorted(rects, key=lambda r: r.size, reverse=True)

    def get_lines(self, x_y: list[tuple[int, int]]) -> list[Line]:
        lines: list[Line] = []
        len_x_y = len(x_y)
        x_y_loop = x_y + [x_y[0]]

        for i in range(len_x_y):
            src = x_y_loop[i]
            dst = x_y_loop[i + 1]

            src_x, src_y = src[0], src[1]
            dst_x, dst_y = dst[0], dst[1]

            lines.append(
                Line(
                    sqrt(((dst_x - src_x) ** 2) + ((dst_y - src_y) ** 2)),
                    src_x,
                    src_y,
                    dst_x,
                    dst_y,
                )
            )

        return sorted(lines, key=lambda l: l.length, reverse=True)

    # pylint: disable=R0914
    def get_pt_2(self, x_y: list[tuple[int, int]]) -> int:
        lines = self.get_lines(x_y)

        for rect in self.get_rects(x_y):
            is_good = True

            src_x, src_y = rect.src_x, rect.src_y
            dst_x, dst_y = rect.dst_x, rect.dst_y

            for line in lines:
                check_src_x, check_src_y = line.src_x, line.src_y
                check_dst_x, check_dst_y = line.dst_x, line.dst_y

                # max of check x is less than min of x
                check_1 = max(check_src_x, check_dst_x) <= min(src_x, dst_x)

                # min of check x is greater than max of x
                check_2 = min(check_src_x, check_dst_x) >= max(src_x, dst_x)

                # max of check y is less than min of y
                check_3 = max(check_src_y, check_dst_y) <= min(src_y, dst_y)

                # min of check y is greater than max of y
                check_4 = min(check_src_y, check_dst_y) >= max(src_y, dst_y)

                if not check_1 and not check_2 and not check_3 and not check_4:
                    is_good = False
                    break

            if is_good:
                break

        return (abs(dst_x - src_x) + 1) * (abs(dst_y - src_y) + 1)

    def solve(self) -> SolveInfo:
        x_y: list[tuple[int, int]] = []

        with open(get_path("09"), encoding="utf-8") as f:
            line = f.readline()

            while line:

                x, y = line.split(",")

                x_y.append((int(x), int(y)))

                line = f.readline()

        return SolveInfo(str(self.get_pt_1(x_y)), str(self.get_pt_2(x_y)))
