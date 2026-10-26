# Selected workspace boundary module from a multi-stage agent workflow.
"""The filesystem boundary for one explicitly selected novel workspace."""
from __future__ import annotations

from pathlib import Path, PureWindowsPath
import os
import stat


def reject_links(path: Path) -> None:
    for item in (path, *path.parents):
        if item.is_symlink():
            raise ValueError(f"workspace path cannot traverse a symbolic link: {item}")
        try:
            info = item.lstat()
        except (FileNotFoundError, NotADirectoryError):
            continue
        if getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0):
            raise ValueError(f"workspace path cannot traverse a junction/reparse point: {item}")
    if path.is_file() and path.stat().st_nlink > 1:
        raise ValueError(f"workspace file cannot be a hard link: {path}")


class WorkspacePaths:
    def __init__(self, root: str | Path):
        supplied = Path(root).expanduser().absolute()
        reject_links(supplied)
        self.root = supplied.resolve()

    def check(self, target: str | Path) -> Path:
        target = Path(target).absolute()
        reject_links(target)
        resolved = target.resolve()
        if not resolved.is_relative_to(self.root):
            raise ValueError(f"write outside novel workspace: {target}")
        return resolved

    def path(self, *parts: str) -> Path:
        for part in parts:
            raw = str(part)
            if (not raw or Path(raw).is_absolute() or PureWindowsPath(raw).drive
                    or ".." in raw.replace("\\", "/").split("/")):
                raise ValueError(f"invalid workspace-relative path: {raw!r}")
        return self.check(self.root.joinpath(*parts))

    def validate_tree(self) -> None:
        if self.root.exists():
            for directory, dirs, files in os.walk(self.root, followlinks=False):
                for name in [*dirs, *files]:
                    self.check(Path(directory) / name)
