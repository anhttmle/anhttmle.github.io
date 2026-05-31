#!/usr/bin/env python3
"""Restore ML post bodies from trantheanh.github.io; keep MyPages front matter."""

from __future__ import annotations

from pathlib import Path

BACKUP = Path("/Users/anhttmle1/workspace/Porfolio/trantheanh.github.io/_posts")
TARGET = Path(__file__).resolve().parent.parent / "_posts"


def extract_front_matter(corrupted: str) -> str:
    lines = corrupted.splitlines()
    if not lines or lines[0].strip() != "---":
        return ""
    out = []
    for line in lines[1:]:
        if line.strip() == "---" or line.startswith("---"):
            out.append("---")
            break
        out.append(line)
    return "\n".join(["---", *out, "---", ""])


def merge_post(name: str) -> None:
    backup = BACKUP / name
    target = TARGET / name
    if not backup.exists():
        print(f"skip (no backup): {name}")
        return
    fm = extract_front_matter(target.read_text(encoding="utf-8"))
    body = backup.read_text(encoding="utf-8")
    if body.startswith("---"):
        parts = body.split("---", 2)
        body = parts[2] if len(parts) >= 3 else body
    if not fm:
        merged = backup.read_text(encoding="utf-8")
    else:
        merged = fm + body.lstrip("\n")
    target.write_text(merged, encoding="utf-8")
    print(f"restored: {name}")


def main() -> None:
    for path in sorted(TARGET.glob("*ML*.md")):
        merge_post(path.name)


if __name__ == "__main__":
    main()
