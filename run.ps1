<#
.SYNOPSIS
    Run all days or specific days in Pytest

.PARAMETER Day
    (Optional) The day to process (e.g., 04).

.EXAMPLE
    .\run.ps1
    Runs all tests.

.EXAMPLE
    .\run.ps1 -Day 04
    Runs tests for Day 04.
#>

param (
    [string]$Day
)

if ($Day -eq "-h" -or $Day -eq "--help") {
    Get-Help $MyInvocation.MyCommand.Path -Detailed
    exit 0
}

if ($Day -and $Day -notmatch "^\d{2}$") {
    Write-Host "Error: Day must be a two-digit number (e.g., 04)." -ForegroundColor Red
    exit 1
}

$testPath = "test/test_run.py"
if ($Day) {
    $testPath += "::test_Day$Day"
}

pipenv run pytest -s $testPath
