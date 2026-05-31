#!/usr/bin/env python3
"""Audit ML posts for non-standard LaTeX / MathJax markup."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

POSTS_DIR = Path(__file__).resolve().parent.parent / "_posts"

UNICODE_MATH = "θα∑ℓ⎮≤≥∞×∆∫≈𝜏"
PROSE_LDOTS = re.compile(r"(?<!\\)\\ldots|\\\\ldots|\\…")
SINGLE_DELIM = re.compile(r"(?<!\\)\\(?=[\(\)\[\]])")
DOUBLE_OK = re.compile(r"\\\\(?=[\(\)\[\]])")
BOLD_MATH = re.compile(
    r"\*\*(?:J'?\(θ\)|J\(θ\)|θ|α|f\(x\)|h\(x\)|y\s*=\s*f\(x\))\*\*"
)
BROKEN = [
    (re.compile(r"\\\\ \\\\"), "delimiter thừa/broken (\\\\ \\\\)"),
    (re.compile(r"\\\\ \\"), "delimiter broken (\\\\ space)"),
    (re.compile(r"\\\\\\"), "quá nhiều backslash (\\\\\\+)"),
    (re.compile(r"\\\\Deltax"), "\\\\Deltax (thiếu khoảng trắng)"),
    (re.compile(r"\\\\\\Delta"), "\\\\\\Delta (delimiter hỏng)"),
    (re.compile(r"\\\\x="), "\\\\x= (delimiter hỏng)"),
]
PIPE_IN_INLINE = re.compile(
    r"\\\\\([^)]*\|[^)]*\\\\\)"
)
PROSE_TIMES = re.compile(r"(?<![\\$])\d+\\times\d+")
MISSING_MATHJAX = re.compile(r"^mathjax:\s*true", re.M)


@dataclass
class Report:
    path: str
    issues: list[str] = field(default_factory=list)


def split_body(text: str) -> str:
    if not text.startswith("---"):
        return text
    parts = text.split("---", 2)
    return parts[2] if len(parts) >= 3 else text


def audit_file(path: Path) -> Report:
    text = path.read_text(encoding="utf-8")
    body = split_body(text)
    rep = Report(path.name)

    if not MISSING_MATHJAX.search(text):
        rep.issues.append("thiếu mathjax: true trong front matter")

    for ch in UNICODE_MATH:
        if ch in body:
            rep.issues.append(f"ký tự Unicode toán: {ch!r}")

    if PROSE_LDOTS.search(body):
        rep.issues.append("\\ldots hoặc \\… trong prose (nên dùng …)")

    singles = list(SINGLE_DELIM.finditer(body))
    if singles:
        rep.issues.append(
            f"delimiter 1 backslash (cần \\\\): {len(singles)} chỗ"
        )

    if BOLD_MATH.search(body):
        rep.issues.append("biến toán còn dạng **bold** chưa chuyển \\( \\)")

    for pat, msg in BROKEN:
        if pat.search(body):
            rep.issues.append(msg)

    for m in PIPE_IN_INLINE.finditer(body):
        snip = body[m.start() : m.end()][:60]
        rep.issues.append(f"| trong inline math (Kramdown table): {snip!r}")

    if PROSE_TIMES.search(body):
        rep.issues.append("\\times giữa số trong prose (nên dùng ×)")

    # align blocks with <=> instead of \\Leftrightarrow
    if re.search(r"<=>\s", body):
        rep.issues.append("<=> trong công thức (nên \\Leftrightarrow)")

    # empty align lines with only \\
    if re.search(r"\$\$\s*\n\\\\\s*\n\\begin\{align", body):
        rep.issues.append("dòng \\\\ thừa sau $$ trước align")

    return rep


def main() -> None:
    reports = [audit_file(p) for p in sorted(POSTS_DIR.glob("*.md"))]
    bad = [r for r in reports if r.issues]

    print(f"Đã quét {len(reports)} bài. Có vấn đề: {len(bad)}\n")
    for r in bad:
        print(f"## {r.path}")
        for issue in r.issues:
            print(f"  - {issue}")
        print()

    ok = [r.path for r in reports if not r.issues]
    if ok:
        print(f"OK ({len(ok)}): {', '.join(ok)}")


if __name__ == "__main__":
    main()
