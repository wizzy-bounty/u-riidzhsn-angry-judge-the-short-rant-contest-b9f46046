"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt (1-400 UTF-8 characters, not only whitespace).

Chosen rant: the family group chat drowned in "good morning" flower
images -- one concrete scene, a real turn (mute it once and suddenly
YOU are the rude one), anger that feels shared rather than performed.
"""

import os

ENTRY = (
    "My family group chat has 214 unread messages and every single one "
    "is a 'good morning' flower. I mute it for one day and suddenly I'm "
    "the rude one who missed grandma's birthday."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
