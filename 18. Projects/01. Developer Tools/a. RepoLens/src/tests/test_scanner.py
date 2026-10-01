from pathlib import Path

from repolens.scanner import RepositoryScanner


def test_scanner_finds_python_files(tmp_path: Path) -> None:
    source = tmp_path / "main.py"
    source.write_text("print('hello')", encoding="utf-8")

    scanner = RepositoryScanner(tmp_path)

    files = scanner.scan()

    assert files == [source]


def test_scanner_ignores_virtual_environment(
    tmp_path: Path,
) -> None:
    source = tmp_path / "main.py"
    source.write_text("print('hello')", encoding="utf-8")

    ignored = tmp_path / ".venv" / "hidden.py"
    ignored.parent.mkdir()
    ignored.write_text("print('ignored')", encoding="utf-8")

    scanner = RepositoryScanner(tmp_path)

    files = scanner.scan()

    assert source in files
    assert ignored not in files