#!/usr/bin/env python3
"""Copy the finished front page into the output folder.

Reads entry.png from this script's own folder and writes it to the folder
named by MAKEFUN_OUTPUT_DIR (or /output when the variable is unset).
Prints the destination path and the file's sha256, and exits non-zero
when the image is missing. Pure standard library, no network.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    with open(dst, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    print("wrote", dst)
    print("sha256", digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
