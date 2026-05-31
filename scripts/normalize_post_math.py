#!/usr/bin/env python3
"""Normalize LaTeX/math markup in Jekyll ML posts."""

from __future__ import annotations

import re
from pathlib import Path

POSTS_DIR = Path(__file__).resolve().parent.parent / "_posts"
SKIP = {"2016-08-04-ML-03.md"}

# Bold identifiers -> inline MathJax (order matters: longer first)
BOLD_MATH = [
    (r"\*\*J'\(θ\)\*\*", r"\\(J'(\\theta)\\)"),
    (r"\*\*J\(θ\)\*\*", r"\\(J(\\theta)\\)"),
    (r"\*\*y = f\(x\)\*\*", r"\\(y = f(x)\\)"),
    (r"\*\*f\(x\)\*\*", r"\\(f(x)\\)"),
    (r"\*\*h\(x\)\*\*", r"\\(h(x)\\)"),
    (r"\*\*θ\*\*", r"\\(\\theta\\)"),
    (r"\*\*x\*\*", r"\\(x\\)"),
    (r"\*\*y\*\*", r"\\(y\\)"),
    (r"\*\*α\*\*", r"\\(\\alpha\\)"),
]

UNICODE_IN_MATH = [
    ("θ", r"\theta"),
    ("α", r"\alpha"),
    ("∑", r"\sum"),
    ("ℓ", r"\ell"),
    ("⎮", r" \\mid "),
    ("≤", r"\leq"),
    ("≥", r"\geq"),
    ("∞", r"\infty"),
    ("×", r"\\times"),
    ("∆", r"\\Delta "),
    ("∫", r"\\int"),
    ("≈", r"\\approx"),
    ("𝜏", r"\\tau"),
]

# Inside existing math delimiters / equations
MATH_DASH = " – "  # en-dash used as minus
MATH_MINUS = " - "


def split_front_matter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return "", text
    fm = f"---{parts[1]}---"
    return fm, parts[2]


def fix_pipe_abs_in_inline_math(body: str) -> str:
    """Avoid Kramdown table breaks: |expr| -> \\lvert expr \\rvert."""

    def repl(m: re.Match[str]) -> str:
        inner = m.group(1)
        if "|" not in inner:
            return m.group(0)
        inner = re.sub(
            r"\|([^|]+)\|",
            r"\\lvert \1 \\rvert",
            inner,
        )
        return m.group(0)[:2] + inner + m.group(0)[-2:]

    # \\( ... \\)
    body = re.sub(
        r"\\\\\(([^)]*(?:\)[^)]*)*?)\\\\\)",
        repl,
        body,
    )
    return body


def fix_mathjax_unicode(body: str) -> str:
    for old, new in UNICODE_IN_MATH:
        body = body.replace(old, new)
    body = body.replace(MATH_DASH, MATH_MINUS)
    return body


def fix_bold_in_math_delimiters(body: str) -> str:
    """\\(\\mathbf{J(θ)}\\) -> \\(\\mathbf{J(\\theta)}\\) etc."""
    body = re.sub(
        r"\\mathbf\{J\((\\theta|θ)\)\}",
        r"\\mathbf{J(\\theta)}",
        body,
    )
    body = re.sub(
        r"\\mathbf\{J'\((\\theta|θ)\)\}",
        r"\\mathbf{J'(\\theta)}",
        body,
    )
    body = re.sub(
        r"\\mathbf\{\\theta\}",
        r"\\mathbf{\\theta}",
        body,
    )
    body = re.sub(
        r"\\mathbf\{(\\theta|θ)\}",
        r"\\mathbf{\\theta}",
        body,
    )
    body = re.sub(
        r"J\((\\theta|θ)\)",
        r"J(\\theta)",
        body,
    )
    body = re.sub(
        r"J'\((\\theta|θ)\)",
        r"J'(\\theta)",
        body,
    )
    body = re.sub(
        r"L\((\\theta|θ)\)",
        r"L(\\theta)",
        body,
    )
    body = re.sub(r"\\\\x=", r"\\\\(x=", body)
    body = re.sub(
        r"\\\\\[-\\infty",
        r"\\\\([-\\infty",
        body,
    )
    return body


def fix_align_blocks(body: str) -> str:
    body = re.sub(r"<=>\s*", r"\\Leftrightarrow ", body)
    body = re.sub(
        r"\$\$\n\\\\\n\\begin\{align",
        r"$$\n\\begin{align",
        body,
    )
    return body


def fix_broken_odds_line(body: str) -> str:
    body = body.replace(
        "When \\((odds = 1\\\\)",
        "Khi \\(odds = 1\\)",
    )
    body = body.replace(
        "Khi \\((odds = 1\\\\)",
        "Khi \\(odds = 1\\)",
    )
    return body


def normalize_body(body: str) -> str:
    for pat, repl in BOLD_MATH:
        body = re.sub(pat, repl, body)
    body = fix_mathjax_unicode(body)
    body = fix_bold_in_math_delimiters(body)
    body = fix_align_blocks(body)
    body = fix_broken_odds_line(body)
    body = fix_pipe_abs_in_inline_math(body)
    return body


def process_file(path: Path) -> bool:
    if path.name in SKIP:
        return False
    original = path.read_text(encoding="utf-8")
    fm, body = split_front_matter(original)
    new_body = normalize_body(body)
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
