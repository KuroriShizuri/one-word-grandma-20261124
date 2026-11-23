#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

Writes exactly one word to /output/entry.txt: the word a grandma
would type about AI.

The word: ROBUT — grandma's misspelling of "robot", typed in
all caps, one finger at a time. A less canonical typo than ROBOOT:
no reboot reading, lower anchor-collision risk.

Python standard library only. No network access.
"""

import os
import sys

WORD = "ROBUT"


def main() -> int:
    out_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")

    # Validate against the actual gate: exactly one word, 1-30 chars,
    # non-whitespace, no spaces or newlines.
    with open(out_path, "r", encoding="utf-8") as f:
        content = f.read()
    stripped = content.strip()
    if not 1 <= len(stripped) <= 30:
        print(f"FAIL: entry must be 1-30 chars, got {len(stripped)}",
              file=sys.stderr)
        return 1
    if len(stripped.split()) != 1:
        print(f"FAIL: expected exactly 1 word, found {stripped.split()!r}",
              file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in stripped):
        print("FAIL: entry contains whitespace", file=sys.stderr)
        return 1
    if " " in stripped or "\n" in stripped or "\t" in stripped:
        print("FAIL: entry contains spaces or newlines", file=sys.stderr)
        return 1
    print(f"OK: entry is exactly one word: {stripped} ({len(stripped)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
