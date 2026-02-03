## Advent of Code 2025

![Build Status](https://github.com/masonpimentel/advent-of-code-2025/actions/workflows/ci.yml/badge.svg) [![codecov](https://codecov.io/gh/masonpimentel/advent-of-code-2025/branch/master/graph/badge.svg)](https://codecov.io/gh/masonpimentel/advent-of-code-2025/)

Python solutions for Advent of Code 2025 (https://adventofcode.com/2025/) with code quality managed by these tools:

* Linting: pylint https://pylint.readthedocs.io/en/stable/
* Typing: mypy https://mypy-lang.org/
* Formatting: black https://black.readthedocs.io/en/stable/

Join my leaderboard! https://adventofcode.com/2025/leaderboard/private: `4780152-1e037a8f` (note you need to be signed in to join private leaderboards)

### Performance

Machines:

| Name | Description |
| --- | --- |
| PC | Intel Core i5 12600K |
| Mac | M4 |
| Github runner | ubuntu-24.04 |

Runtime (seconds):

| Day | Status | PC | Mac | Github runner |
| ----- | --- | --- | --- | --- |
| Day 1 | 🟢 | < 0.1 | < 0.1 | < 0.1 |
| Day 2 | 🟡 | ~ 1.5 | ~ 1 | ~ 2 |
| Day 3 | 🟢 | < 0.1 | < 0.1 | < 0.1 |
| Day 4 | 🔵 | < 0.1 | < 0.1 | ~ 0.5 |
| Day 5 | 🟢 | < 0.1 | < 0.1 | < 0.1 |
| Day 6 | 🟢 | < 0.1 | < 0.1 | < 0.1 |
| Day 7 | 🟢 | < 0.1 | < 0.1 | < 0.1 |
| Day 8 | 🔵 | ~ 0.5 | ~ 0.5 | ~ 1 |
| Day 9 | 🔵 | ~ 0.5 | ~ 0.5 | ~ 0.5 |
| Day 10 | 🟡 | ~ 1.5 | ~ 1 | ~ 2.5 |
| Day 11 | 🟢 | < 0.1 | < 0.1 | < 0.1 |
| Day 12 | 🟢 | < 0.1 | < 0.1 | < 0.1 |

### Install packages

Only dev packages are needed so use `--dev`

`pipenv install --dev`

### Running

Run using `pytest` and see solution output

#### Mac

Use `./run.sh`

#### Windows

Use `.\run.ps1`

### Formatting

CI will check that all files are formatted according to `black`

To ensure CI will pass, run `pipenv run black --check .`

### MyPy

`pipenv run mypy src`

### Pylint

`pipenv run pylint src`

### To run all the above

Use `./run-all.sh` or `.\run-all.ps1`

### To get average time over n runs

`pipenv run pytest -s test --runs n`

Example for the average over 3 runs: `pipenv run pytest -s test --runs 3`
