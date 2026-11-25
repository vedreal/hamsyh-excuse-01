"""The One-Line AI Excuse for Breaking Production.

Writes the entry line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os
from pathlib import Path

ENTRY = (
    "Your database is gone, but I saved a copy in my context window. "
    "It's 200,000 tokens and I can only remember the first line."
)


def output_path() -> Path:
    """Return the path the entry text must be written to."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(base) / "entry.txt"


def main() -> None:
    """Write the entry line to the output file."""
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
