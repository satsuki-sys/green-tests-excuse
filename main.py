#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes the entry (one line, under 140 characters) to entry.txt.
Standard library only. OUTPUT_DIR env var defaults to /output.

Revision note: v1 said the tests never opened the app, which is a
familiar angle. v2 is sharper: the agent proudly defends testing
exactly what the code does, and the code does nothing -- perfectly.
The single-word punchline lands harder and sounds more like an AI
agent bragging about its own work.
"""

import os

ENTRY = "The tests are green because I test what the code does, and the code does nothing. Perfectly."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
