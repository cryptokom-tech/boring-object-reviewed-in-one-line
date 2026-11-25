"""The Most Boring Object, Reviewed in One Line — entry program.

Writes one line (a review of the window blinds, under 200 characters)
to /output/entry.txt. Python 3.13, standard library only. Deterministic:
the same line every run. The written file is read back and verified
byte-for-byte before the program reports success.
"""

import os
import sys

LINE = (
    "The blinds' one job is blocking the sun, and they do it by letting "
    "in exactly one stripe of light, directly into your eyes, at 6 a.m. "
    "One star."
)


def main() -> int:
    line = LINE
    if not line or len(line) > 200:
        return 1
    if "\n" in line or "\r" in line:
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        if f.read() != line:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
