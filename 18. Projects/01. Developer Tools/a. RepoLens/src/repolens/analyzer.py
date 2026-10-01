"""Python source-code analysis using the standard-library AST module."""

import ast
from pathlib import Path

from .models import ClassInfo, FunctionInfo, ModuleInfo, RepositoryReport
from .scanner import RepositoryScanner


class PythonAnalyzer:
    """Analyze individual Python source files."""

    def analyze_file(self, path: Path, root: Path) -> ModuleInfo:
        """Parse and analyze one Python file."""
        relative_path = path.relative_to(root)
        module_name = self._module_name(relative_path)

        try:
            source = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            return ModuleInfo(
                path=relative_path,
                module_name=module_name,
                lines=0,
                errors=[f"UTF-8 decoding failed: {exc}"],
            )
        except OSError as exc:
            return ModuleInfo(
                path=relative_path,
                module_name=module_name,
                lines=0,
                errors=[f"Could not read file: {exc}"],
            )

        lines = len(source.splitlines())

        try:
            tree = ast.parse(source, filename=str(path))
        except SyntaxError as exc:
            return ModuleInfo(
                path=relative_path,
                module_name=module_name,
                lines=lines,
                errors=[
                    f"Syntax error at line {exc.lineno}: {exc.msg}"
                ],
            )

        imports = self._extract_imports(tree)
        functions = self._extract_functions(tree)
        classes = self._extract_classes(tree)

        return ModuleInfo(
            path=relative_path,
            module_name=module_name,
            lines=lines,
            imports=imports,
            functions=functions,
            classes=classes,
        )

    def analyze_repository(
        self,
        root: Path,
        scanner: RepositoryScanner,
    ) -> RepositoryReport:
        """Analyze every Python file in a repository."""
        report = RepositoryReport(root=root)

        for path in scanner.scan():
            module = self.analyze_file(path, root)

            if module.errors:
                report.skipped_files.append(
                    f"{module.path}: {'; '.join(module.errors)}"
                )

            report.python_files.append(module)

        return report

    @staticmethod
    def _module_name(relative_path: Path) -> str:
        """Convert a relative Python path into a readable module name."""
        parts = list(relative_path.parts)

        if parts[-1] == "__init__.py":
            parts = parts[:-1]
        else:
            parts[-1] = relative_path.stem

        return ".".join(parts) or "__root__"

    @staticmethod
    def _extract_imports(tree: ast.AST) -> list[str]:
        """Extract imported module names."""
        imports: list[str] = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.extend(alias.name for alias in node.names)

            elif isinstance(node, ast.ImportFrom):
                module = node.module or "."

                for alias in node.names:
                    imports.append(f"{module}.{alias.name}")

        return sorted(set(imports))

    @staticmethod
    def _extract_functions(tree: ast.AST) -> list[FunctionInfo]:
        """Extract top-level and nested function definitions."""
        functions: list[FunctionInfo] = []

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                functions.append(
                    FunctionInfo(
                        name=node.name,
                        line=node.lineno,
                        is_async=isinstance(
                            node,
                            ast.AsyncFunctionDef,
                        ),
                    )
                )

        return sorted(functions, key=lambda item: item.line)

    @staticmethod
    def _extract_classes(tree: ast.AST) -> list[ClassInfo]:
        """Extract classes and their direct methods."""
        classes: list[ClassInfo] = []

        for node in ast.walk(tree):
            if not isinstance(node, ast.ClassDef):
                continue

            methods = [
                child.name
                for child in node.body
                if isinstance(
                    child,
                    (ast.FunctionDef, ast.AsyncFunctionDef),
                )
            ]

            classes.append(
                ClassInfo(
                    name=node.name,
                    line=node.lineno,
                    methods=methods,
                )
            )

        return sorted(classes, key=lambda item: item.line)