#!/usr/bin/env bash

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
  cat <<EOF
Usage: ./run.sh [-h|--help]
Runs code quality checks:
- Format: black
- Type check: mypy
- Lint: pylint
- Tests: pytest
EOF
  exit 0
fi

pipenv run black --check .
pipenv run mypy src
pipenv run pylint src
pipenv run pytest -s test
