#!/usr/bin/env bash

show_help() {
    cat << EOF
Usage: ${0##*/} [-d DAY] [-a ACTION]
Process a Python file for a specific day by either formatting or linting or checking types.

Positional Arguments:
  DAY                   The day to process (e.g., 04). This parameter is required.
  ACTION                The action to perform. Can be "format", "lint" or "type". This parameter is required.

Options:
  -d, --day DAY         The day to process.
  -a, --action ACTION   The action to perform.
  -h, --help            Show this help message and exit.

Example:
  ./${0##*/} -d 04 -a format
  Formats the Python file for Day 04.

Example:
  ./${0##*/} -d 04 -a lint
  Lints the Python file for Day 04.

Example:
  ./${0##*/} -d 04 -a type
  Checks types for the Python file for Day 04.
EOF
}

DAY=""
ACTION=""
POSITIONAL=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        -d|--day)
            DAY="$2"
            shift 2
            ;;
        -a|--action)
            ACTION="$2"
            shift 2
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        -*)
            echo "Unknown option: $1"
            show_help
            exit 1
            ;;
        *)
            POSITIONAL+=("$1")  # Collect positional arguments
            shift
            ;;
    esac
done

# If positional arguments were provided, use them if not already set
if [[ ${#POSITIONAL[@]} -ge 1 && -z "$DAY" ]]; then
    DAY="${POSITIONAL[0]}"
fi
if [[ ${#POSITIONAL[@]} -ge 2 && -z "$ACTION" ]]; then
    ACTION="${POSITIONAL[1]}"
fi

# Ensure required arguments are provided
if [[ -z "$DAY" || -z "$ACTION" ]]; then
    echo "Error: Both day and action are required."
    echo
    show_help
    exit 1
fi

if [[ ! "$DAY" =~ ^[0-9]{2}$ ]]; then
    echo "Error: Day must be a two-digit number (e.g., 04)."
    echo
    show_help
    exit 1
fi

# Construct the file path
FILE_PATH="src/solvers/d$DAY/d$DAY.py"

# Check if the file exists
if [[ ! -f "$FILE_PATH" ]]; then
    echo "Error: File '$FILE_PATH' does not exist."
    echo
    show_help
    exit 1
fi

# Perform the specified action
case "$ACTION" in
    format)
        echo "Formatting file: $FILE_PATH"
        pipenv run black "$FILE_PATH"
        ;;
    lint)
        echo "Linting file: $FILE_PATH"
        pipenv run pylint "$FILE_PATH"
        ;;
    type)
        echo "Checking types for file: $FILE_PATH"
        pipenv run mypy "$FILE_PATH"
        ;;
    *)
        echo "Error: Unknown action '$ACTION'. Valid actions are 'format', 'lint', or 'type'."
        exit 1
        ;;
esac