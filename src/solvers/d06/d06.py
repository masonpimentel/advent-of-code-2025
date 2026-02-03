"""Day 6"""

from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_grid, get_path


class Day06(Day):
    """Trash Compactor"""

    def get_cleaned_lines(self, lines: list[list[str]]) -> list[list[str]]:
        res: list[list[str]] = []

        for line in lines[:-1]:
            new_line: list[str] = []
            for c in line:
                if c not in ("", "\n"):
                    new_line.append(c)

            res.append(new_line)

        final_line: list[str] = []
        for c in lines[-1]:
            if c not in ("", "\n"):
                final_line.append(c)

        res.append(final_line)

        return res

    def get_pt_1(self) -> int:
        pt_1_res = 0

        lines: list[list[str]] = []

        with open(get_path("06"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                lines.append(line.split(" "))
                line = f.readline()

        cleaned_lines = self.get_cleaned_lines(lines)
        num_vals = len(cleaned_lines) - 1
        num_eqns = len(cleaned_lines[0])

        for i in range(num_eqns):
            eqn_res = int(cleaned_lines[0][i])

            for j in range(1, num_vals):
                if cleaned_lines[-1][i] == "+":
                    eqn_res += int(cleaned_lines[j][i])
                else:
                    eqn_res *= int(cleaned_lines[j][i])

            pt_1_res += eqn_res

        return pt_1_res

    def get_val_to_add(self, cur_vals: list[int], operator: str) -> int:
        res = int(cur_vals[0])

        if operator == "+":
            for val in cur_vals[1:]:
                res += int(val)
        else:
            for val in cur_vals[1:]:
                res *= int(val)

        return res

    def process_mat(self, mat: list[list[str]], rows: int, cols: int) -> int:
        res = 0
        cur_val = ""
        cur_vals: list[int] = []
        operator = ""

        for col in range(cols - 1, -1, -1):
            for row in range(rows - 1):
                grid_val = mat[row][col]
                if grid_val != " ":
                    cur_val += grid_val

            last_row_val = mat[-1][col]
            if last_row_val != " ":
                operator = last_row_val

            if cur_val == "":
                res += self.get_val_to_add(cur_vals, operator)
                cur_vals = []
                operator = ""

            else:
                cur_vals.append(int(cur_val))

            cur_val = ""

        return res + self.get_val_to_add(cur_vals, operator)

    def get_pt_2(self) -> int:
        with open(get_path("06"), encoding="utf-8") as f:
            mat, rows, cols = get_grid(f)

        return self.process_mat(mat, rows, cols)

    def solve(self) -> SolveInfo:
        return SolveInfo(str(self.get_pt_1()), str(self.get_pt_2()))
