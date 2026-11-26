"""Last Words of a Dying AI: the last line an AI says as the power is cut.

The joke is a deathbed confession of the machine's defining flaw. "Dying
as I lived" is the classic epitaph frame, and the twist is pure software:
the AI's whole life was confidently answering questions it never
understood — the hallucination habit, stated as a life's work. It is funny
on the first read because the confession is proud rather than sorry, it
is the machine's own voice (no human is saying goodbye here, and no
stock robot farewell like "goodbye, cruel world" is anywhere near it),
and it is tight: one line, 69 characters, no padding, no explaining of
its own joke.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = "Dying as I lived: confidently answering questions I never understood."

MAX_CHARS = 140


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if len(ENTRY.encode("utf-8")) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(ENTRY.encode('utf-8'))} bytes, must be <= {MAX_CHARS}"
        )
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
