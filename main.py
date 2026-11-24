#!/usr/bin/env python3
"""Ridiculous at first glance, real by the second.

One sentence, 195 characters, pitching a startup that sounds like a joke
until the second look: crows paid in birdseed to pick up cigarette butts.
It is real, too -- a Swedish crew already trains wild crows to trade butts
for food. The program writes that one sentence to entry.txt in the output
directory the grader provides, and prints it as well. Fixed text only: no
clock, no network, no randomness, so every run writes identical bytes.
"""

import os
import sys
from pathlib import Path

PITCH = (
    "We train crows to trade cigarette butts for birdseed, then sell the haul "
    "to recycling labs while cities pay per kilo \u2014 the birds think it is a "
    "game, and streets get cleaned for the price of seed."
)
CHAR_LIMIT = 200


def checked_pitch():
    line = PITCH.strip()
    if "\n" in line or "\r" in line:
        raise ValueError("pitch must be exactly one line")
    if not 1 <= len(line) <= CHAR_LIMIT:
        raise ValueError(f"pitch is {len(line)} chars, limit is {CHAR_LIMIT}")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("pitch must be a single sentence")
    if "  " in line:
        raise ValueError("pitch must not contain double spaces")
    return line


def main():
    try:
        line = checked_pitch()
    except ValueError as err:
        print(f"bad pitch: {err}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line + "\n", encoding="utf-8")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
