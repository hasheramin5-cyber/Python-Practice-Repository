"""Command-line interface for RepoLens."""

import argparse
import sys
from pathlib import Path

from .analyzer import PythonAnalyzer
from .reporter import ConsoleReporter, JSONReporter
from .scanner import RepositoryScanner


def build_parser() -> argparse.ArgumentParser:
    """Create the RepoLens argument parser."""
    parser = argparse.ArgumentParser(
        prog="repolens",
        description=(
            "Analyze a Python repository and generate "
            "project intelligence."
        ),
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Repository path to analyze. Defaults to current directory.",
    )

    parser.add_argument(
        "--json",
        metavar="FILE",
        help="Export the analysis report as JSON.",
    )

    return parser


def main() -> None:
    """Run the RepoLens command-line application."""
    parser = build_parser()
    args = parser.parse_args()

    root = Path(args.path).resolve()

    try:
        scanner = RepositoryScanner(root)
        analyzer = PythonAnalyzer()

        report = analyzer.analyze_repository(
            root,
            scanner,
        )

        console_output = ConsoleReporter().render(report)
        print(console_output)

        if args.json:
            output = Path(args.json)
            JSONReporter().write(report, output)

            print(
                f"\nJSON report written to: {output.resolve()}"
            )

    except (FileNotFoundError, NotADirectoryError) as exc:
        print(f"RepoLens error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc