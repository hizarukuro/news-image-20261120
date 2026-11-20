#!/usr/bin/env python3
"""Entry program for the news-image-20261120 make.fun competition.

The entry is a single newspaper front page (entry.png) summing up the
world news of Friday 20 November 2026. This program's only job is to
deliver that image: it copies entry.png, byte for byte, into the
directory named by the MAKEFUN_OUTPUT_DIR environment variable, or
into a local "output" directory when the variable is not set.

Standard library only — the grading environment has no third-party
packages installed.
"""

import os
import shutil
import sys

SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(here, "output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, OUTPUT_NAME)

    if not os.path.isfile(source):
        print(f"error: {SOURCE_NAME} not found next to main.py", file=sys.stderr)
        return 1

    shutil.copyfile(source, target)

    src_size = os.path.getsize(source)
    if os.path.getsize(target) != src_size:
        print("error: delivered file size does not match the source", file=sys.stderr)
        return 1
    print(f"delivered {OUTPUT_NAME} ({src_size} bytes) to {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
