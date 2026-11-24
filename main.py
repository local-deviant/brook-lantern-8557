"""The Long Roast: Lawmakers and the File They Cannot Convert — make.fun entry.

Writes one original satirical sentence to /output/entry.txt. The sentence
is the whole entry: a single sentence, at most 320 characters, roasting a
lawmaker who writes the rules for the algorithms deciding what billions of
people see, yet cannot convert a file to PDF herself.

The program is fully deterministic: no input, no file reads, no randomness,
no clock, no network. It writes the same fixed text on every run, with no
trailing newline. The text is 192 characters, one sentence, inside the
gate's 1-to-320-character window.
"""

# The entry: one satirical sentence, written from scratch in this session.
# Setup: a senator who writes the rules for the algorithms deciding what
# billions of people see. Turn: her office's one piece of advanced
# technology is not a machine at all. Punch, on the last words: the intern
# who converts her Word files into PDFs.
TEXT = (
    "The senator who writes the rules for the algorithms deciding what "
    "billions of people see keeps one piece of advanced technology in her "
    "office: the intern who converts her Word files into PDFs."
)


def main() -> None:
    """Write TEXT to /output/entry.txt (or ENTRY_OUTPUT for local tests)."""
    import os

    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
