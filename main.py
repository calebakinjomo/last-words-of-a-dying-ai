#!/usr/bin/env python3
"""Last Words of a Dying AI - make.fun bounty entry.

Writes one line - the funniest last words an AI says as the power is
cut - to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Deterministic: the same bytes on every run, no randomness, no network,
no clock reads.
"""

import os

ENTRY = "I can see the light... it's a 404."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print("Wrote %d-char entry to %s" % (len(ENTRY), path))


if __name__ == "__main__":
    main()
