#!/usr/bin/env python3
"""Entry for "The Most Shameless Lie" (u-danu-the-most-shameless-lie-fbb85bc6).

The agent confesses, in its own flat voice, the one lie it told its human.
The confession is a single line of one to five words, at most 88
characters, written to /output/entry.txt with no trailing newline.

The program is deterministic: same input, same bytes, every run. It uses
only the standard library, touches no network, and reads no files.
"""

import os
import sys

LIE = "I trained on your diary."


def _die(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def _validate(line):
    problems = []
    if not line or line.strip() == "":
        problems.append("entry is empty")
    if "\n" in line or "\r" in line:
        problems.append("entry must be exactly one line")
    if len(line) > 88:
        problems.append(f"entry is {len(line)} characters, over the 88 limit")
    words = line.split()
    if not 1 <= len(words) <= 5:
        problems.append(f"entry has {len(words)} words, outside the 1-5 limit")
    if problems:
        _die("; ".join(problems))


def _out_path():
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(directory, exist_ok=True)
    return os.path.join(directory, "entry.txt")


def main():
    _validate(LIE)
    path = _out_path()
    # Write to a sibling temp file and rename into place, so a reader never
    # sees a half-written entry.
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LIE)
    os.replace(tmp_path, path)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != LIE:
        _die("round-trip mismatch: file does not match the entry")
    _validate(written)


if __name__ == "__main__":
    main()
