"""Make the AI Judge Feel Proud: A Family Scene — make.fun entry.

Writes one short family scene (a single line of text) to
``/output/entry.txt``. The program is fully deterministic: no input,
no network, no randomness, no clock. It only validates the scene
against the competition gate (UTF-8 text, 1-280 characters, not only
whitespace, a single line ending in sentence punctuation) and writes
it out exactly, with no trailing newline.
"""

import os

TEXT = (
    "Mum still saves Dad the last dumpling every night, "
    "Dad still pretends not to notice, "
    "and I still pretend I never saw — "
    "some love languages come with chopsticks."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280
SENTENCE_ENDINGS = (".", "!", "?")


def check(text):
    """Validate the scene against the competition gate.

    Returns a list of error messages; an empty list means the text
    is valid.
    """
    errors = []
    if not isinstance(text, str):
        errors.append("entry must be a string")
        return errors
    if not text:
        errors.append("entry is empty")
    if not text.strip():
        errors.append("entry is only whitespace")
    if len(text) > MAX_CHARS:
        errors.append(
            "entry is %d characters, over the %d-character limit"
            % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        errors.append("entry must be a single line")
    if text and not text.endswith(SENTENCE_ENDINGS):
        errors.append("entry must end with sentence punctuation")
    return errors


def run():
    """Validate the scene and write it to /output/entry.txt."""
    errors = check(TEXT)
    if errors:
        raise ValueError("; ".join(errors))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    run()
