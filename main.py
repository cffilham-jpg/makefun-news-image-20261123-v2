#!/usr/bin/env python3
"""news-image-20261123 entry (Python 3.13, standard library only).

Copies the pre-rendered poster entry.png beside this file to the output
directory: MAKEFUN_OUTPUT_DIR when set, otherwise /output (the grader's
writable output directory). The repository is read-only at grading time,
so this program only reads entry.png and writes to the output directory.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1024 * 1024


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(SRC, "rb") as f:
        data = f.read()
    if not data.startswith(PNG_SIGNATURE):
        raise ValueError("entry.png is not a PNG file")
    if len(data) > MAX_BYTES:
        raise ValueError("entry.png exceeds the 1 MiB cap")
    dest = os.path.join(out_dir, "entry.png")
    with open(dest, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
