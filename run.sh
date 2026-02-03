#!/usr/bin/env bash

show_help() {
    cat << EOF
Usage: ${0##*/} [DAY]
Run all days or specific days in Pytest

Positional Arguments:
  DAY               (Optional) The day to process (e.g., 04).

Options:
  -h, --help        Show this help message and exit.

Example:
  ./${0##*/}
  Runs all days

Example:
  ./${0##*/} 04 
  Runs Day 04
EOF
}

# Check for help flag
if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    show_help
    exit 0
fi

pipenv run pytest -s "test/test_run.py${1:+::test_Day$1}"