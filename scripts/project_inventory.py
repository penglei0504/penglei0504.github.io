#!/usr/bin/env python3
"""Read-only inventory of project reference files; no third-party packages."""

import argparse
import hashlib
import json
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
MEDIA = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".mp4", ".webm", ".mov", ".avi"}


def inventory(source, manifest):
    source = source.resolve()
    if not source.is_dir():
        raise ValueError(f"Source directory does not exist: {source}")
    saved = json.loads(manifest.read_text(encoding="utf-8")) if manifest.exists() else {"version": 1, "projects": {}}
    if saved.get("version") != 1 or not isinstance(saved.get("projects"), dict):
        raise ValueError("Expected manifest version 1 with a projects mapping")
    current = {}
    warnings = []
    # Never follow source symlinks/junctions to files outside the reference folder.
    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        if not path.resolve().is_relative_to(source):
            warnings.append(f"Skipped reference outside source folder: {path.name}")
            continue
        relative = path.relative_to(source)
        if any(part.startswith(".") for part in relative.parts):
            continue
        group = relative.parts[0] if len(relative.parts) > 1 else "."
        item = relative.relative_to(group).as_posix() if group != "." else relative.as_posix()
        record = current.setdefault(group, {"files": {}, "media": [], "large_files": []})
        digest = hashlib.sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
        record["files"][item] = digest.hexdigest()
        size = path.stat().st_size
        if path.suffix.lower() in MEDIA:
            record["media"].append({"path": item, "bytes": size})
        if size > 20 * 1024 * 1024:
            record["large_files"].append({"path": item, "bytes": size, "action": "Review before publishing; do not copy automatically"})
    for group, record in current.items():
        previous = saved["projects"].get(group)
        record["state"] = "new" if previous is None else "unchanged" if previous.get("files") == record["files"] else "changed"
    missing = sorted(set(saved["projects"]) - set(current))
    return {"source": str(source), "groups": current, "missing_source_groups": missing,
            "warnings": warnings, "note": "Inventory only. No files were written or deleted; source groups are not automatically publishable projects."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=REPO / "My_project")
    parser.add_argument("--manifest", type=Path, default=REPO / "_data/project_sources.json")
    args = parser.parse_args()
    try:
        result = inventory(args.source, args.manifest)
    except (OSError, ValueError, TypeError) as error:
        print(f"Inventory error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
