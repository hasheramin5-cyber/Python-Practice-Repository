"""Human-readable and JSON reporting."""

import json
from dataclasses import asdict
from pathlib import Path

from .models import RepositoryReport


class ConsoleReporter:
    """Render repository analysis in the terminal."""

    def render(self, report: RepositoryReport) -> str:
        """Build a readable terminal report."""
        lines = [
            "",
            "RepoLens",
            "========",
            f"Repository : {report.root}",
            "",
            "Summary",
            "-------",
            f"Python files : {report.total_files}",
            f"Source lines : {report.total_lines}",
            f"Functions    : {report.total_functions}",
            f"Classes      : {report.total_classes}",
            f"Imports      : {report.total_imports}",
            "",
            "Modules",
            "-------",
        ]

        if not report.python_files:
            lines.append("No Python files found.")
            return "\n".join(lines)

        for module in report.python_files:
            lines.append(
                f"\n{module.path}"
                f"  ({module.lines} lines)"
            )

            if module.imports:
                lines.append(
                    "  Imports: "
                    + ", ".join(module.imports)
                )

            if module.classes:
                for class_info in module.classes:
                    method_text = ", ".join(class_info.methods)

                    if method_text:
                        lines.append(
                            f"  Class: {class_info.name}"
                            f" (methods: {method_text})"
                        )
                    else:
                        lines.append(
                            f"  Class: {class_info.name}"
                        )

            if module.functions:
                for function in module.functions:
                    prefix = "async " if function.is_async else ""
                    lines.append(
                        f"  Function: {prefix}"
                        f"{function.name} "
                        f"(line {function.line})"
                    )

            if module.errors:
                for error in module.errors:
                    lines.append(f"  Error: {error}")

        if report.skipped_files:
            lines.extend(
                [
                    "",
                    "Warnings",
                    "--------",
                ]
            )

            lines.extend(
                f"- {item}"
                for item in report.skipped_files
            )

        return "\n".join(lines)


class JSONReporter:
    """Export repository analysis as JSON."""

    def write(
        self,
        report: RepositoryReport,
        output: Path,
    ) -> None:
        """Write the report to a JSON file."""
        payload = {
            "repository": str(report.root),
            "summary": {
                "python_files": report.total_files,
                "source_lines": report.total_lines,
                "functions": report.total_functions,
                "classes": report.total_classes,
                "imports": report.total_imports,
            },
            "modules": [
                {
                    **asdict(module),
                    "path": str(module.path),
                }
                for module in report.python_files
            ],
            "warnings": report.skipped_files,
        }

        output.parent.mkdir(parents=True, exist_ok=True)

        output.write_text(
            json.dumps(payload, indent=2),
            encoding="utf-8",
        )