#!/usr/bin/env python3
"""The Printer Finally Answers — one line, the office printer's comeback.

The printer has kept an error log all day. It reads it back, flatly.
"""
import os
import sys

ENTRY = (
    "My error log for today: paper jam, low toner, and one (1) human "
    "who thumped me and called it troubleshooting."
)


def validate(text):
    """Mirror the sealed gate: UTF-8 text, 1-240 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 240:
        raise ValueError(f"entry must be 1-240 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return True


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
