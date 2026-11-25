"""The 3AM Fridge Text — one line a smart fridge texts its owner at 3am.

Writes a single-line text message to /output/entry.txt.

The line: the fridge is the only appliance still awake at 3am, still
cold, and — having watched its owner eat the last slice standing up in
the dark — it refuses to pretend it saw nothing. A fresh angle (the
fridge as a witness with opinions), no milk, no ice, no door left open.
"""

import os
import sys

# The entry: one line, well under the 140-character gate.
ENTRY = (
    "It's 3am. I'm the only one in this house still awake, still cold, "
    "and done pretending I didn't watch you eat the last slice standing up."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read it back and enforce the gate ourselves before exiting.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            f"entry is {len(text)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if text.strip() == "" or "\n" in text or "\r" in text:
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    print(f"wrote {len(text)}-character entry to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
