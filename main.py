"""Write the one-word internet entry to /output/entry.txt.

The gate accepts UTF-8 text of 1 to 30 characters, so the entry is
validated here before it is written.
"""

import os

OUT = os.environ.get("MAKEFUN_OUT", "/output")

# The pick: the internet is the fridge you open when bored, find nothing
# new inside, and open again five minutes later anyway.
ENTRY = "fridge"


def main() -> None:
    if not 1 <= len(ENTRY) <= 30:
        raise ValueError("entry must be 1 to 30 characters")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY:
        raise ValueError("entry must be a single non-blank line")
    if len(ENTRY.split()) != 1:
        raise ValueError("entry must be exactly one word")
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):
        path = os.path.join(OUT, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as handle:
        # No trailing newline: the file holds exactly the entry line.
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
