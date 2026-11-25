#!/usr/bin/env python3
"""Pigeon Pitch, One Line — write the entry line to /output/entry.txt.

Reads MAKEFUN_OUTPUT_DIR when set (default /output). Writes exactly the
entry line with no trailing newline. Exits non-zero if the line is empty,
whitespace-only, over 200 characters, or contains CR/LF.
"""

import os
import sys
from pathlib import Path

ENTRY_LINE = (
    # Why this line: "seed" does double duty — birdseed for the pigeons,
    # a seed round for the investors — and the split mirrors the pitch:
    # pigeons see lunch, investors see recurring revenue.
    "Investors, we turn sidewalk crumbs into recurring revenue; "
    "pigeons call it lunch, your analysts call it seed funding."
)


def validate(line: str) -> str | None:
    """Return an error message if the line is invalid, else None."""
    if not line or not line.strip():
        return "entry line is empty or whitespace-only"
    if len(line) > 200:
        return f"entry line is {len(line)} chars, over the 200-char limit"
    if "\r" in line or "\n" in line:
        return "entry line must be a single line (contains CR/LF)"
    return None


def main() -> int:
    error = validate(ENTRY_LINE)
    if error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY_LINE, encoding="utf-8")
    print(f"wrote {len(ENTRY_LINE)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
