#!/usr/bin/env python3
"""Double-escape \\( \\) \\[ \\] for Kramdown → MathJax HTML."""

from __future__ import annotations

import re
from pathlib import Path

POSTS_DIR = Path(__file__).resolve().parent.parent / "_posts"

DELIMITER_PATTERNS = [
    (re.compile(r"(?<!\\)\\(?=\()"), r"\\\\"),
    (re.compile(r"(?<!\\)\\(?=\))"), r"\\\\"),
    (re.compile(r"(?<!\\)\\(?=\[)"), r"\\\\"),
    (re.compile(r"(?<!\\)\\(?=\])"), r"\\\\"),
]


def split_front_matter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return "", text
    return f"---{parts[1]}---", parts[2]


def fix_body(body: str) -> str:
    for pattern, repl in DELIMITER_PATTERNS:
        body = pattern.sub(repl, body)
    return body


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    fm, body = split_front_matter(original)
    new_body = fix_body(body)
    if new_body == body:
        return False
    path.write_text(fm + new_body, encoding="utf-8")
    return True


def main() -> None:
    changed = []
    for path in sorted(POSTS_DIR.glob("*.md")):
        if process_file(path):
            changed.append(path.name)
    print(f"Updated {len(changed)} files:")
    for name in changed:
        print(f"  - {name}")


if __name__ == "__main__":
    main()
