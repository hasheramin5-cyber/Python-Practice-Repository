"""Data models used by RepoLens."""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class FunctionInfo:
    """Information about a Python function."""

    name: str
    line: int
    is_async: bool = False


@dataclass
class ClassInfo:
    """Information about a Python class."""

    name: str
    line: int
    methods: list[str] = field(default_factory=list)


@dataclass
class ModuleInfo:
    """Information extracted from one Python module."""

    path: Path
    module_name: str
    lines: int
    imports: list[str] = field(default_factory=list)
    functions: list[FunctionInfo] = field(default_factory=list)
    classes: list[ClassInfo] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def function_count(self) -> int:
        """Return the number of functions in the module."""
        return len(self.functions)

    @property
    def class_count(self) -> int:
        """Return the number of classes in the module."""
        return len(self.classes)


@dataclass
class RepositoryReport:
    """Complete analysis result for a repository."""

    root: Path
    python_files: list[ModuleInfo] = field(default_factory=list)
    skipped_files: list[str] = field(default_factory=list)

    @property
    def total_files(self) -> int:
        """Return the number of Python files discovered."""
        return len(self.python_files)

    @property
    def total_functions(self) -> int:
        """Return the total number of functions."""
        return sum(module.function_count for module in self.python_files)

    @property
    def total_classes(self) -> int:
        """Return the total number of classes."""
        return sum(module.class_count for module in self.python_files)

    @property
    def total_lines(self) -> int:
        """Return the total number of source lines."""
        return sum(module.lines for module in self.python_files)

    @property
    def total_imports(self) -> int:
        """Return the number of import statements."""
        return sum(len(module.imports) for module in self.python_files)