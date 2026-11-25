#!/usr/bin/env python3
"""The Funniest Honest Appliance Error.

Writes one line of plain text (at most 200 characters): the funniest
honest error message an appliance could show. Here a dishwasher reports
the most common fault it sees: plates loaded facing the wall, so the
spray arms wash the wall instead of the plates.

Deterministic: the same text on every run, no network, no randomness.
"""

import os

TEXT = (
    "ERROR D07: You loaded every plate facing the wall. I washed the "
    "wall instead. The plates are still dirty. This is on you."
)


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
