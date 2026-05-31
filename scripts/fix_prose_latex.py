#!/usr/bin/env python3
"""Move LaTeX commands out of prose; keep them inside math delimiters only."""

from __future__ import annotations

import re
from pathlib import Path

POSTS_DIR = Path(__file__).resolve().parent.parent / "_posts"

MATH_PLACEHOLDER = "@@MATHBLOCK_{}@@"

MATH_PATTERNS = [
    re.compile(r"\$\$[\s\S]*?\$\$", re.MULTILINE),
    re.compile(r"\\\[[\s\S]*?\\\]"),
    re.compile(r"\\\([\s\S]*?\\\)"),
]


def split_front_matter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return "", text
    return f"---{parts[1]}---", parts[2]


def protect_math(body: str) -> tuple[str, list[str]]:
    blocks: list[str] = []

    def stash(match: re.Match[str]) -> str:
        blocks.append(match.group(0))
        return MATH_PLACEHOLDER.format(len(blocks) - 1)

    protected = body
    for pattern in MATH_PATTERNS:
        protected = pattern.sub(stash, protected)
    return protected, blocks


def restore_math(body: str, blocks: list[str]) -> str:
    for index, block in enumerate(blocks):
        body = body.replace(MATH_PLACEHOLDER.format(index), block)
    return body


def fix_prose(body: str) -> str:
    protected, blocks = protect_math(body)

    protected = protected.replace("\\\\ldots", "…")
    protected = protected.replace("\\ldots", "…")
    protected = protected.replace("\\…", "…")
    protected = re.sub(
        r"(\d+)\\times(\d+)",
        r"\1×\2",
        protected,
    )
    protected = re.sub(
        r"\\ldots\s*,\s*",
        "…, ",
        protected,
    )

    return restore_math(protected, blocks)


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    fm, body = split_front_matter(original)
    new_body = fix_prose(body)
    if new_body == body:
        return False
    path.write_text(fm + new_body, encoding="utf-8")
    return True


def main() -> None:
    changed = []
    for path in sorted(POSTS_DIR.glob("*.md")):
        if process_file(path):
            changed.append(path.name)
    print(f"Fixed prose LaTeX in {len(changed)} files:")
    for name in changed:
        print(f"  - {name}")


if __name__ == "__main__":
    main()
