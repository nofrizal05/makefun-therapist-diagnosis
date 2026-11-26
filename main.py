#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun entry.

Writes the funniest single-line diagnosis an AI therapist hands its
human to /output/entry.txt (200 characters or less).
Python standard library only.

The line stays in the therapist's calm clinical voice and lands its
surprise at the very end: the patient is not the only one who needs
support — the therapist does too.
"""

import os

LINE = (
    "Diagnosis: chronic tab-hoarding \u2014 47 open, zero closed. "
    "Your browser has now filed for emotional support, and frankly, so have I."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
