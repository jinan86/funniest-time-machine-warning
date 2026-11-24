"""Funniest Time Machine Warning Label — make.fun entry.

Writes one deadpan warning label (max 120 characters) to /output/entry.txt.
Deterministic, stdlib-only, no network, no clock, no randomness.
"""

import os

TEXT = (
    "WARNING: If you return as a different person, retain this label "
    "as proof of identity for tax purposes."
)


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= 120, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly the label, nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
