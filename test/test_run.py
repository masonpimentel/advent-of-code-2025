from solvers.d01.d01 import Day01
from solvers.d02.d02 import Day02
from solvers.d03.d03 import Day03
from solvers.d04.d04 import Day04
from solvers.d05.d05 import Day05
from solvers.d06.d06 import Day06
from solvers.d07.d07 import Day07
from solvers.d08.d08 import Day08
from solvers.d09.d09 import Day09
from solvers.d10.d10 import Day10
from solvers.d11.d11 import Day11
from solvers.d12.d12 import Day12

import time

EXPECTED_RESULTS = {
    "01": ("1078", "6412"),
    "02": ("19574776074", "25912654282"),
    "03": ("17493", "173685428989126"),
    "04": ("1543", "9038"),
    "05": ("789", "343329651880509"),
    "06": ("5877594983578", "11159825706149"),
    "07": ("1649", "16937871060075"),
    "08": ("54180", "25325968"),
    "09": ("4781546175", "1573359081"),
    "10": ("486", "17820"),
    "11": ("607", "506264456238938"),
    "12": ("433", "NO_PT_2"),
}


def do_run(d, expected: str, times: list[float]):
    start = time.perf_counter()
    res = d.solve()
    end = time.perf_counter()

    assert res[0] == expected[0]
    assert res[1] == expected[1]

    elapsed = end - start
    times.append(elapsed)

    return res


def runner(d, day_str: str, runs: int = 1):
    print(f"\nRunning Day {day_str}")
    expected = EXPECTED_RESULTS[day_str]

    # Warm-up
    d.solve()

    times = []
    if runs == 1:
        res = do_run(d, expected, times)
        print(f"Elapsed {times[-1]:.03f} seconds")
    else:
        for i in range(runs):
            res = do_run(d, expected, times)
            print(f"Run {i + 1}: {times[-1]:.03f}s")

        avg = sum(times) / runs
        print(f"Average over {runs} runs: {avg:.03f}s")

    print(f"pt_1_res: {res[0]}")
    print(f"pt_2_res: {res[1]}")


def test_Day01(runs):
    runner(Day01(), "01", runs)


def test_Day02(runs):
    runner(Day02(), "02", runs)


def test_Day03(runs):
    runner(Day03(), "03", runs)


def test_Day04(runs):
    runner(Day04(), "04", runs)


def test_Day05(runs):
    runner(Day05(), "05", runs)


def test_Day06(runs):
    runner(Day06(), "06", runs)


def test_Day07(runs):
    runner(Day07(), "07", runs)


def test_Day08(runs):
    runner(Day08(), "08", runs)


def test_Day09(runs):
    runner(Day09(), "09", runs)


def test_Day10(runs):
    runner(Day10(), "10", runs)


def test_Day11(runs):
    runner(Day11(), "11", runs)


def test_Day12(runs):
    runner(Day12(), "12", runs)
