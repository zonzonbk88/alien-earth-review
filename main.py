#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one alien tourist's one-line review of planet Earth to
/output/entry.txt (1-200 chars, single line, plain UTF-8 text).
Standard library only.
"""

import os

ENTRY = (
    "Beautiful planet. The locals invented 8,000 languages and still "
    "mostly communicate by sending each other cat pictures. "
    "5/5, would visit again."
)


def main() -> None:
    line = " ".join(ENTRY.split())
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
