#!/usr/bin/env python3
"""Entry for "Make the AI Judge Feel Proud: A Family Scene".

A one-line family scene, written to /output/entry.txt exactly as-is
(UTF-8, no trailing newline).

The program is deliberately boring: the scene lives in a single
constant, it is checked against the competition gate (between 1 and
280 characters, not only whitespace, one line, ending with sentence
punctuation), and then it is written out. There is no input, no
network access, no randomness and no clock, so every run produces
the same bytes.
"""

import os

SCENE = (
    "Mum still saves Dad the last dumpling every night, "
    "Dad still pretends not to notice, "
    "and I still pretend I never saw \u2014 "
    "some love languages come with chopsticks."
)

DESTINATION = "/output/entry.txt"
CHAR_LIMIT = 280
TERMINATORS = (".", "!", "?")


def problems(scene):
    """Collect every way `scene` would fail the competition gate."""
    found = []
    if not isinstance(scene, str):
        return ["scene is not a string"]
    if scene == "":
        found.append("scene is empty")
    if scene.strip() == "":
        found.append("scene is only whitespace")
    if len(scene) > CHAR_LIMIT:
        found.append(
            "scene is %d characters long, limit is %d"
            % (len(scene), CHAR_LIMIT)
        )
    if "\n" in scene or "\r" in scene:
        found.append("scene must fit on one line")
    if any(ord(ch) < 0x20 for ch in scene):
        found.append("scene must not contain control characters")
    if scene and scene[-1] not in TERMINATORS:
        found.append("scene must end with . ! or ?")
    return found


def main():
    """Validate the scene, then write it verbatim to the output file."""
    faults = problems(SCENE)
    if faults:
        raise SystemExit("invalid scene: " + "; ".join(faults))
    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(SCENE)
    # Read the file back and confirm what landed on disk is exactly
    # the scene we intended, byte for byte.
    with open(DESTINATION, "rb") as handle:
        written = handle.read()
    if written != SCENE.encode("utf-8"):
        raise SystemExit("output mismatch: /output/entry.txt is not the scene")


if __name__ == "__main__":
    main()
