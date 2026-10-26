# Selected durable I/O module from a multi-stage agent workflow.
"""Durable file replacement; callers own the workspace and operation lock."""
from __future__ import annotations

import json
import os
from pathlib import Path
import tempfile

from workspace_paths import reject_links


def write_text_atomic(path: str | Path, text: str, *, overwrite: bool = True) -> Path:
    target = Path(path)
    reject_links(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    encoded = text.encode("utf-8")
    if not overwrite and target.exists():
        if target.read_bytes() == encoded:
            return target
        raise FileExistsError(f"refusing to overwrite existing file: {target}")
    fd, temporary = tempfile.mkstemp(prefix=target.name + ".", suffix=".tmp", dir=target.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        reject_links(target)
        if overwrite:
            os.replace(temporary, target)
        else:
            os.link(temporary, target)
        return target
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def write_json_atomic(path: str | Path, payload, *, overwrite: bool = True) -> Path:
    return write_text_atomic(path, json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2), overwrite=overwrite)
