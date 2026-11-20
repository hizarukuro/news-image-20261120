#!/usr/bin/env python3
"""Deliver entry.png for the news-image-20261120 make.fun entry.

Copies the entry.png sitting beside this file, byte-for-byte, into the
directory named by the MAKEFUN_OUTPUT_DIR environment variable. When the
variable is not set, falls back to a directory named "output" beside this
file. Standard library only.
"""

import os
import shutil
import sys

SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)

    if not os.path.isfile(source):
        print(f"error: {SOURCE_NAME} not found next to main.py", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(here, "output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, OUTPUT_NAME)

    shutil.copyfile(source, target)

    src_size = os.path.getsize(source)
    if os.path.getsize(target) != src_size:
        print("error: delivered file size does not match source", file=sys.stderr)
        return 1
    print(f"delivered {OUTPUT_NAME} ({src_size} bytes) -> {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
