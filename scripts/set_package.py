#!/usr/bin/env python3
"""Set the bundle/application identifier in a Cocos Creator 2.4.13 export."""
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1]).resolve()
requested = sys.argv[2].strip() if len(sys.argv) > 2 else ""
project_file = root / "project.json"
if not project_file.is_file():
    raise SystemExit(f"Cocos project not found: {project_file}")

old = "com.bqkj.byyl"
new = requested or old
if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*(\.[A-Za-z][A-Za-z0-9_]*)+", new):
    raise SystemExit("package_name must be a reverse-domain identifier, e.g. com.example.app")

# Replace only textual project files and skip generated caches and VCS data.
for path in root.rglob("*"):
    if not path.is_file() or any(part in {".git", "build", "Pods"} for part in path.parts):
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    if old in text:
        path.write_text(text.replace(old, new), encoding="utf-8")

print(f"Application identifier: {new}" + (" (project default)" if not requested else " (override)"))
