"""Day 8"""

from heapq import heappush, heappop
from math import sqrt
from collections import Counter
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


class Day08(Day):
    """Playground"""

    def __init__(self) -> None:
        self.parent: list[int] = []
        self.rank: list[int] = []
        self.groups = 0

    def find(self, i: int) -> int:
        root = self.parent[i]

        if self.parent[root] != root:
            self.parent[i] = self.find(root)
            return self.parent[i]

        return root

    def unite(self, i: int, j: int) -> None:
        irep = self.find(i)
        jrep = self.find(j)

        if irep == jrep:
            return

        if self.rank[irep] < self.rank[jrep]:
            self.parent[irep] = jrep
        elif self.rank[jrep] < self.rank[irep]:
            self.parent[jrep] = irep
        else:
            self.parent[jrep] = irep
            self.rank[irep] += 1

        self.groups -= 1

    def get_pt_1(self, h: list[tuple[int, int, int]], len_coords: int) -> int:
        for _ in range(1000):
            if len(h) == 0:
                break

            _, i, j = heappop(h)

            self.unite(i, j)

        c: Counter[int] = Counter()

        for i in range(len_coords):
            parent = self.find(i)

            c[parent] += 1

        v = sorted(list(c.values()), reverse=True)

        return v[0] * v[1] * v[2]

    def get_pt_2(
        self, h: list[tuple[int, int, int]], coords: list[tuple[int, int, int]]
    ) -> int:
        while True:
            _, i, j = heappop(h)

            self.unite(i, j)

            if self.groups == 1:
                junction_1 = coords[i]
                junction_2 = coords[j]

                return junction_1[0] * junction_2[0]

    def solve(self) -> SolveInfo:
        coords: list[tuple[int, int, int]] = []

        with open(get_path("08"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                s = [int(v) for v in line.split(",")]
                coords.append((s[0], s[1], s[2]))

                line = f.readline()

        len_coords = len(coords)

        h_1: list[tuple[int, int, int]] = []
        h_2: list[tuple[int, int, int]] = []

        for i in range(len_coords):
            for j in range(i + 1, len_coords):
                src = coords[i]
                dst = coords[j]
                d = int(
                    sqrt(
                        ((src[0] - dst[0]) ** 2)
                        + ((src[1] - dst[1]) ** 2)
                        + ((src[2] - dst[2]) ** 2)
                    )
                )
                heappush(h_1, (d, i, j))
                heappush(h_2, (d, i, j))

        self.parent = list(range(len_coords))
        self.rank = [0] * len_coords
        self.groups = len_coords

        pt_1_res = self.get_pt_1(h_1, len_coords)

        self.parent = list(range(len_coords))
        self.rank = [0] * len_coords
        self.groups = len_coords

        return SolveInfo(str(pt_1_res), str(self.get_pt_2(h_2, coords)))
