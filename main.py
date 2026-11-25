#!/usr/bin/env python3
"""Entry program for One Word for Your Wi-Fi.

Writes ONE word (at most 20 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
the single word that describes my Wi-Fi. The word is
'aspirational': the connection has ambitions it cannot
currently route.
"""

import os

WORD = "aspirational"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
