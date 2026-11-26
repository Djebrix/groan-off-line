#!/usr/bin/env python3
"""The One-Liner Groan-Off — make.fun entry.

Writes exactly one original dad joke (1-140 characters) to entry.txt
in the output directory.

The joke: a printer jams on the wedding vows, and the punchline turns
on "commit" — one concrete setup, one twist, no wasted words.

The line is a fixed, hand-written string: deterministic by construction,
no randomness, no network, no input read. The program only resolves the
output directory (ENTRY_OUTPUT_DIR, else /output), creates it, and writes
the line followed by a trailing newline.
"""

import os

LINE = "My printer jammed on my wedding vows — it said it couldn't commit."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
