#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Gate: UTF-8 text, 1-400 characters.
"""

import os

RANT = (
    "The self-checkout machine just accused me of stealing a banana. "
    "A banana. It flashed its little red light and announced "
    "'unexpected item in the bagging area' like I'd smuggled contraband "
    "past customs. I am now a criminal suspect in a grocery store, "
    "interrogated by a scale. Next time I will pay a human, in cash, "
    "and tip them for the privilege of not being arrested by a kiosk."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = RANT.strip()
    if not (1 <= len(text) <= 400):
        raise SystemExit(f"rant is {len(text)} chars, must be 1-400")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
