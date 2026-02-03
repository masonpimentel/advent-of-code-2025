<#
.SYNOPSIS
    Process a Python file for a specific day by either formatting or linting or checking types.

.PARAMETER Day
    The day to process (e.g., 04). This parameter is required.

.PARAMETER Action
    The action to perform. Can be "format", "lint" or "type". This parameter is required.

.EXAMPLE
    .\process-file.ps1 -Day 04 -Action format
    Formats the Python file for Day 04.

    .\process-file.ps1 -Day 04 -Action lint
    Lints the Python file for Day 04.

    .\process-file.ps1 -Day 04 -Action type
    Checks types for the Python file for Day 04.
#>

param (
    [Parameter(Mandatory = $true, HelpMessage = "Please provide the day (e.g., -Day 04).")]
    [string]$Day,

    [Parameter(Mandatory = $true, HelpMessage = "Specify the action: 'format', 'lint' or 'type'.")]
    [ValidateSet("format", "lint", "type")]
    [string]$Action
)

# Display help message if needed
if ($Day -eq "-h" -or $Day -eq "--help") {
    Get-Help $MyInvocation.MyCommand.Path -Detailed
    exit 0
}

# Validate that Day is a two-digit number
if ($Day -notmatch "^\d{2}$") {
    Write-Host "Error: Day must be a two-digit number (e.g., 04)." -ForegroundColor Red
    exit 1
}

# Construct the file path
$FilePath = "src\solvers\d$Day\d$Day.py"

# Check if the file exists
if (-Not (Test-Path $FilePath)) {
    Write-Host "Error: File '$FilePath' does not exist." -ForegroundColor Red
    exit 1
}

# Perform the specified action
switch ($Action) {
    "format" {
        Write-Host "Formatting file: $FilePath" -ForegroundColor Cyan
        pipenv run black $FilePath
    }
    "lint" {
        Write-Host "Linting file: $FilePath" -ForegroundColor Cyan
        pipenv run pylint $FilePath
    }
    "type" {
        Write-Host "Checking types for file: $FilePath" -ForegroundColor Cyan
        pipenv run mypy $FilePath
    }
}