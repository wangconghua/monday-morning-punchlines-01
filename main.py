#!/usr/bin/env python3
"""Monday Morning Punchlines (make.fun entry).

The joke: five alarms are set for Monday morning, and the twist is a
reversal of agency -- the alarms hit snooze on the sleeper instead of
the other way round. It is plainly about a Monday morning, it earns its
laugh from the turn in the last words, it says it in one short sentence,
and it leans on no tired Monday cliche (no coffee, no "I hate Mondays",
no "case of the Mondays").
"""

import os

JOKE = "I set five alarms for Monday morning, and all five hit snooze on me."

OUT_PATH = "/output/entry.txt"

# Gate (from the kit's RULES.txt): /output/entry.txt must be UTF-8 text of
# 1 to 200 characters, not only white space. main() enforces the same bound
# here so a bad edit fails loudly instead of submitting an invalid entry.
MIN_CHARS = 1
MAX_CHARS = 200

# Judge criterion 1: the joke must really be about Monday mornings.
MONDAY_TOKENS = ("monday morning", "monday mornings")

# Judge criterion 5: worn-out Monday lines that flood a field of one-line
# entries. Any of these in the text means the entry is playing a joke
# everyone has already heard.
CLICHES = ("case of the mondays", "i hate mondays", "i hate monday",
           "back to the grind", "rise and grind", "here we go again",
           "weekend is over", "weekend's over", "mondays, am i right",
           "coffee", "garfield", "back to work", "another monday",
           "oh no, it's monday", "monday again")


def _check_gate(text):
    """Gate checks from the kit's RULES.txt: 1-200 characters, one line,
    not only whitespace, valid UTF-8, no leading/trailing space and no
    double spaces. A bad entry must fail loudly here, before any of the
    judge-criterion checks run, so a broken edit never reaches the
    output file looking like a valid submission.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text)))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "  " in text:
        raise ValueError("entry must be tight: no double spaces")


def _check_monday_morning(text):
    """Judge criterion 1: the joke must be about Monday mornings, not a
    stray line about another day or topic.
    """
    lowered = text.lower()
    if not any(token in lowered for token in MONDAY_TOKENS):
        raise ValueError("entry must be a joke about Monday mornings")


def _check_fresh(text):
    """Judge criterion 5: the wording must feel fresh, not a rerun of
    the tired Monday cliches everyone has heard.
    """
    lowered = text.lower()
    for cliche in CLICHES:
        if cliche in lowered:
            raise ValueError("entry uses a tired Monday cliche: %r" % cliche)


def _check_single_sentence(text):
    """Judge criteria 2 and 4: one sentence, clear on one reading, with
    the punchline landing at the end rather than up front.
    """
    body = text[:-1] if text[-1] in ".!?" else text
    if any(mark in body for mark in (".", "!", "?", ";", ":")):
        raise ValueError("entry must be a single sentence")
    if not text.endswith("hit snooze on me."):
        raise ValueError("entry must land its punchline in the last words")


def _check_read_aloud(text):
    """Judge criterion 4: the line must survive being read aloud once.
    At most 30 words, and the setup (everything before the comma) at
    most 12 words, so the twist is not buried behind a long clause.
    """
    words = text.split()
    if len(words) > 30:
        raise ValueError(
            "entry must read aloud in one breath (<=30 words), got %d"
            % len(words))
    setup, _, _ = text.partition(",")
    if len(setup.split()) > 12:
        raise ValueError("entry setup must stay short: at most 12 words")


def validate(text):
    """Fail loudly if the entry would fail the gate or lose on the judge's
    own criteria. Returns the validated text unchanged.

    Gate: 1-200 characters, one line, not only whitespace, valid UTF-8.
    Judge: really about Monday mornings (criterion 1), a real laugh with
    the turn landing in the last words (criterion 2), a surprising twist
    (criterion 3: the alarms snooze the sleeper), few words with every
    word doing work (criterion 4: one short sentence), and fresh wording
    (criterion 5: no tired Monday cliche).
    """
    _check_gate(text)
    _check_monday_morning(text)
    _check_fresh(text)
    _check_single_sentence(text)
    _check_read_aloud(text)
    return text


def main():
    validate(JOKE)
    out_dir = "/output" if os.path.isdir("/output") else os.path.dirname(
        os.path.abspath(__file__))
    out = os.path.join(out_dir, "entry.txt")
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    with open(out, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != JOKE:
        raise ValueError("written entry does not match the validated text")
    validate(written)
    print("wrote %s: %d characters" % (out, len(JOKE)))


if __name__ == "__main__":
    main()
