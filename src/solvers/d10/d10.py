"""Day 10"""

from sys import maxsize, setrecursionlimit
from math import gcd
from itertools import product

from typing import NamedTuple
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


setrecursionlimit(10**6)


# pylint: disable=C0115
class Machine(NamedTuple):
    needed_on: str
    needed_joltage: list[int]
    buttons: list[list[int]]


# pylint: disable=C0115
class LinearEqnParts(NamedTuple):
    counter_effects: list[list[int]]
    target_counts: list[int]
    max_button_presses: list[int]


class EliminateArgs(NamedTuple):
    counter_effects: list[list[int]]
    target_counts: list[int]
    pivot_row: int
    target_row: int
    pivot_col: int


class ProcessPivotColsArgs(NamedTuple):
    pivot_cols: list[int]
    running_sum: int
    best: int
    counter_effects: list[list[int]]
    target_counts: list[int]
    free_cols: list[int]
    press_counts: list[int]


class Day10(Day):
    """Factory"""

    def __init__(self) -> None:
        self.dp: dict[str, int] = {}

    def rec(
        self, target: str, cur: str, possible: list[list[int]], seen: set[str]
    ) -> int:
        if cur in seen:
            return maxsize

        if cur in self.dp:
            return self.dp[cur]

        if cur == target:
            return 0

        seen.add(cur)

        res = maxsize
        for p in possible:
            new = "".join(
                "1" if ((v == "0" and i in p) or (v == "1" and i not in p)) else "0"
                for i, v in enumerate(cur)
            )
            this_res = self.rec(target, new, possible, seen)
            res = min(res, this_res + 1)

        seen.discard(cur)

        self.dp[cur] = res
        return res

    def build_linear_eqn(self, machine: Machine) -> LinearEqnParts:
        len_buttons = len(machine.buttons)

        target_counts = machine.needed_joltage

        len_counters = len(target_counts)

        counter_effects = [[0 for _ in range(len_buttons)] for _ in range(len_counters)]
        max_button_presses = [maxsize] * len_buttons

        for button_idx, button in enumerate(machine.buttons):
            for counter in button:
                counter_effects[counter][button_idx] = 1

            max_button_presses[button_idx] = min(
                target_counts[button_val] for button_val in button
            )

        return LinearEqnParts(counter_effects, target_counts, max_button_presses)

    def swap_rows(
        self, counter_effects: list[list[int]], target_counts: list[int], i: int, j: int
    ) -> None:
        if i != j:
            counter_effects[i], counter_effects[j] = (
                counter_effects[j],
                counter_effects[i],
            )
            target_counts[i], target_counts[j] = target_counts[j], target_counts[i]

    def eliminate(self, args: EliminateArgs) -> None:
        counter_effects, target_counts, pivot_row, target_row, pivot_col = args

        p = counter_effects[pivot_row][pivot_col]
        t = counter_effects[target_row][pivot_col]

        if t == 0:
            return

        g = gcd(p, t)
        alpha = t // g
        beta = -p // g

        row_p = counter_effects[pivot_row]
        row_t = counter_effects[target_row]

        counter_effects[target_row] = [
            (alpha * row_p[k]) + (beta * row_t[k]) for k in range(len(row_t))
        ]
        target_counts[target_row] = (alpha * target_counts[pivot_row]) + (
            beta * target_counts[target_row]
        )

    def reduce_integer(
        self, counter_effects: list[list[int]], target_counts: list[int]
    ) -> tuple[list[list[int]], list[int], list[int]]:
        m, n = len(counter_effects), len(counter_effects[0])
        pivot_cols: list[int] = []
        pivot_row = 0

        for col in range(n):
            pivot_r = None
            for r in range(pivot_row, m):
                if counter_effects[r][col] != 0:
                    pivot_r = r
                    break

            if pivot_r is None:
                continue

            self.swap_rows(counter_effects, target_counts, pivot_row, pivot_r)

            for r in range(pivot_row + 1, m):
                self.eliminate(
                    EliminateArgs(counter_effects, target_counts, pivot_row, r, col)
                )

            pivot_cols.append(col)
            pivot_row += 1
            if pivot_row == m:
                break

        new_a, new_b = [], []
        for row, rhs in zip(counter_effects, target_counts):
            if all(v == 0 for v in row):
                if rhs != 0:
                    return [], [], []
                continue
            new_a.append(row)
            new_b.append(rhs)

        return new_a, new_b, pivot_cols

    def back_substitute(
        self,
        counter_effects: list[list[int]],
        target_counts: list[int],
        pivot_cols: list[int],
    ) -> None:
        for pivot_row in range(len(pivot_cols) - 1, -1, -1):
            pivot_col = pivot_cols[pivot_row]

            for r in range(pivot_row):
                self.eliminate(
                    EliminateArgs(
                        counter_effects, target_counts, pivot_row, r, pivot_col
                    )
                )

    def process_pivot_cols(self, args: ProcessPivotColsArgs) -> int:
        (
            pivot_cols,
            running_sum,
            best,
            counter_effects,
            target_counts,
            free_cols,
            press_counts,
        ) = args

        for row_idx, pivot_col in enumerate(pivot_cols):
            diag = counter_effects[row_idx][pivot_col]

            if diag == 0:
                return maxsize

            rhs = target_counts[row_idx]

            for free_col in free_cols:
                rhs -= counter_effects[row_idx][free_col] * press_counts[free_col]

            if rhs % diag != 0:
                return maxsize

            val = rhs // diag
            if val < 0:
                return maxsize

            running_sum += val
            if running_sum >= best:
                return maxsize

        return running_sum

    def solve_min_sum(
        self,
        counter_effects: list[list[int]],
        target_counts: list[int],
        pivot_cols: list[int],
        max_button_presses: list[int],
    ) -> int:
        if not counter_effects:
            return 0

        n = len(counter_effects[0])
        pivot_set = set(pivot_cols)
        free_cols = [j for j in range(n) if j not in pivot_set]
        free_bounds = [max_button_presses[j] for j in free_cols]
        best = maxsize

        for free_vals in product(*(range(b + 1) for b in free_bounds)):
            press_counts = [0] * n

            running_sum = 0
            for col, val in zip(free_cols, free_vals):
                press_counts[col] = val
                running_sum += val

            if running_sum >= best:
                continue

            best = min(
                best,
                self.process_pivot_cols(
                    ProcessPivotColsArgs(
                        pivot_cols,
                        running_sum,
                        best,
                        counter_effects,
                        target_counts,
                        free_cols,
                        press_counts,
                    )
                ),
            )

        return 0 if best == maxsize else best

    def process_machines(self, machines: list[Machine]) -> tuple[int, int]:
        pt_1_res = 0
        pt_2_res = 0

        for machine in machines:
            self.dp = {}
            pt_1_res += self.rec(
                machine.needed_on, "0" * len(machine.needed_on), machine.buttons, set()
            )

            linear_eqn = self.build_linear_eqn(machine)

            counter_effects, target_counts, pivot_cols = self.reduce_integer(
                linear_eqn.counter_effects, linear_eqn.target_counts
            )

            self.back_substitute(counter_effects, target_counts, pivot_cols)

            pt_2_res += self.solve_min_sum(
                counter_effects,
                target_counts,
                pivot_cols,
                linear_eqn.max_button_presses,
            )

        return (pt_1_res, pt_2_res)

    def solve(self) -> SolveInfo:
        machines: list[Machine] = []

        with open(get_path("10"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                parts = line.split(" ")

                needed_on = "".join("1" if v == "#" else "0" for v in parts[0][1:-1])
                buttons = [[int(v) for v in p[1:-1].split(",")] for p in parts[1:-1]]

                raw_joltage = parts[-1]
                needed_joltage = [
                    int(v)
                    for v in raw_joltage[
                        1 : -2 if raw_joltage[-1] == "\n" else -1
                    ].split(",")
                ]

                machines.append(Machine(needed_on, needed_joltage, buttons))

                line = f.readline()

        pt_1_res, pt_2_res = self.process_machines(machines)

        return SolveInfo(str(pt_1_res), str(pt_2_res))
