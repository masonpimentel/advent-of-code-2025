param (
    [string]$Help
)

if ($Help -eq "-h" -or $Help -eq "--help") {
    @"
Usage: .\run.ps1 [-h|--help]
Runs code quality checks:
- Format: black
- Type check: mypy
- Lint: pylint
- Tests: pytest
"@
    exit 0
}

pipenv run black --check .
pipenv run mypy src
pipenv run pylint src
pipenv run pytest -s test
