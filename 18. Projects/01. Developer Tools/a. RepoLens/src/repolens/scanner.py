"""Repository file discovery."""

from pathlib import Path


DEFAULT_IGNORED_DIRECTORIES = {
    ".git",
    ".hg",
    ".svn",
    "__pycache__",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "dist",
    "build",
    ".idea",
    ".pytest_cache",
}


class RepositoryScanner:
    """Find Python source files inside a repository."""

    def __init__(
        self,
        root: Path,
        ignored_directories: set[str] | None = None,
    ) -> None:
        self.root = root.resolve()
        self.ignored_directories = (
            ignored_directories
            if ignored_directories is not None
            else DEFAULT_IGNORED_DIRECTORIES
        )

    def scan(self) -> list[Path]:
        """Return all Python files that should be analyzed."""
        if not self.root.exists():
            raise FileNotFoundError(
                f"Repository path does not exist: {self.root}"
            )

        if not self.root.is_dir():
            raise NotADirectoryError(
                f"Repository path is not a directory: {self.root}"
            )

        python_files: list[Path] = []

        for path in self.root.rglob("*.py"):
            if self._should_skip(path):
                continue

            python_files.append(path)

        return sorted(python_files)

    def _should_skip(self, path: Path) -> bool:
        """Return True when a path belongs to an ignored directory."""
        try:
            relative = path.relative_to(self.root)
        except ValueError:
            return True

        return any(
            part in self.ignored_directories
            for part in relative.parts
        )