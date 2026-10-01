from pathlib import Path

from repolens.analyzer import PythonAnalyzer


def test_analyzer_extracts_python_structure(
    tmp_path: Path,
) -> None:
    source = tmp_path / "example.py"

    source.write_text(
        """
import os
from pathlib import Path


class Example:
    def run(self):
        return Path.cwd()


def hello(name):
    return f"Hello {name}"
""".strip(),
        encoding="utf-8",
    )

    analyzer = PythonAnalyzer()

    result = analyzer.analyze_file(
        source,
        tmp_path,
    )

    assert result.lines == 11
    assert "os" in result.imports
    assert "pathlib.Path" in result.imports
    assert result.class_count == 1
    assert result.function_count == 2
    assert result.classes[0].name == "Example"
    assert result.classes[0].methods == ["run"]


def test_analyzer_handles_syntax_error(
    tmp_path: Path,
) -> None:
    source = tmp_path / "broken.py"

    source.write_text(
        "def broken(:\n",
        encoding="utf-8",
    )

    analyzer = PythonAnalyzer()

    result = analyzer.analyze_file(
        source,
        tmp_path,
    )

    assert result.errors
    assert "Syntax error" in result.errors[0]