"""Day 12"""

from typing import NamedTuple
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


# pylint: disable=C0115
class Tree(NamedTuple):
    width: int
    height: int
    needed: list[int]


class Day12(Day):
    """Christmas Tree Farm"""

    NUM_SHAPES = 6

    def __init__(self) -> None:
        self.shapes: list[int] = []

    def solve_tree(self, t: Tree) -> bool:
        space_needed = 0

        for shape_idx, shape_count in enumerate(t.needed):
            space_needed += self.shapes[shape_idx] * shape_count

        return t.width * t.height >= space_needed

    def process_tree(self, l: str) -> Tree:
        parts = l.split(" ")

        size = parts[0][:-1]
        width, height = size.split("x")
        needed = [int(p) for p in parts[1:]]

        return Tree(int(width), int(height), needed)

    def solve(self) -> SolveInfo:
        self.shapes = [0] * self.NUM_SHAPES
        trees: list[Tree] = []
        line_idx = 0
        shape_idx = 0
        in_trees = False

        with open(get_path("12"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                if in_trees:
                    trees.append(self.process_tree(line))
                else:
                    line_mod = line_idx % 5

                    if line_idx > 0 and line_mod == 0:
                        shape_idx += 1

                        if shape_idx == self.NUM_SHAPES:
                            trees.append(self.process_tree(line))
                            in_trees = True
                    elif 1 <= line_mod <= 3:
                        for col in range(3):
                            self.shapes[shape_idx] += 1 if line[col] == "#" else 0

                line_idx += 1
                line = f.readline()

        pt_1_res = 0
        for t in trees:
            pt_1_res += 1 if self.solve_tree(t) else 0

        return SolveInfo(str(pt_1_res), "NO_PT_2")
