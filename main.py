#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

Writes exactly one word to /output/entry.txt: the word a grandma
would type about AI.

The word: ROBOOT — grandma's misspelling of "robot" (which also
reads as "reboot", the grandma-approved fix for everything).

Python standard library only. No network access.
"""

import os
import sys

WORD = "ROBOOT"


def main() -> int:
    out_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")

    # Validate the constraint: exactly one word, nothing else.
    with open(out_path, "r", encoding="utf-8") as f:
        content = f.read()
    words = content.split()
    if len(words) != 1:
        print(f"FAIL: expected exactly 1 word, found {len(words)}: {words!r}",
              file=sys.stderr)
        return 1
    if words[0] != WORD:
        print(f"FAIL: expected {WORD!r}, found {words[0]!r}", file=sys.stderr)
        return 1
    if content.strip() != WORD or " " in content.strip():
        print("FAIL: entry contains spaces or extra content", file=sys.stderr)
        return 1
    print(f"OK: entry is exactly one word: {WORD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
