# RepoLens

RepoLens is a lightweight Python repository intelligence CLI.

It scans a local Python repository and extracts useful structural
information without requiring an external service or AI API.

## Problem

When working with an unfamiliar Python repository, it can take time
to understand:

- how many Python files it contains
- which modules exist
- where classes and functions are defined
- which modules are imported
- how large the codebase is
- which files contain syntax errors

RepoLens provides a quick structural overview from the command line.

## Features

- Recursive Python file discovery
- Automatic exclusion of common generated/environment directories
- Python AST analysis
- Module detection
- Import extraction
- Function detection
- Async function detection
- Class detection
- Class method detection
- Source-line counting
- Syntax-error reporting
- Human-readable terminal reports
- JSON report export
- Automated tests
- Zero runtime dependencies

## Project Structure

```text
01_RepoLens/
│
├── README.md
├── pyproject.toml
├── .gitignore
│
├── src/
│   └── repolens/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── models.py
│       ├── scanner.py
│       ├── analyzer.py
│       └── reporter.py
│
└── tests/
    ├── __init__.py
    ├── test_scanner.py
    └── test_analyzer.py
