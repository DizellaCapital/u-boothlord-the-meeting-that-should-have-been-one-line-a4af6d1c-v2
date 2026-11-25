#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line — entry V2.

Writes a single sentence that replaces one useless meeting to
MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt as fallback).

Standard library only. No network, no external dependencies.
"""

import os
import sys

ENTRY = (
    "Priya moved the launch to Friday, the client signed off on Thursday, "
    "and this meeting is Wednesday asking for a permission slip nobody needs."
)

SENTENCE_ENDINGS = (".", "!", "?")


def validate(line: str) -> None:
    """Enforce the bounty rules: one line, 1-200 chars, no tab,
    ends with sentence punctuation."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if "\t" in line:
        raise ValueError("entry must not contain tabs")
    if not 1 <= len(line) <= 200:
        # Bounty cap is 200 characters; this entry is 141.
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if not line.endswith(SENTENCE_ENDINGS):
        raise ValueError("entry must end with sentence punctuation")


def main() -> int:
    validate(ENTRY)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")

    # Verify by reading back: exactly one line, identical content.
    with open(out_path, "r", encoding="utf-8") as fh:
        content = fh.read()
    lines = content.splitlines()
    if len(lines) != 1 or lines[0] != ENTRY:
        raise ValueError("read-back verification failed")
    validate(lines[0])

    print(f"wrote {out_path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
