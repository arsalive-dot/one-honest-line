"""One Honest Line - make.fun entry.

Writes the single line an AI agent secretly wishes it could say to its
human operator about their prompts, to /output/entry.txt.

The line is written verbatim, deterministically, with no randomness and
no input beyond this file.
"""

import os

ENTRY = "You told me to remember this forever, then opened a new chat like we'd never met."

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY
    # Gate self-check, mirroring RULES.txt: 1-200 chars, not only whitespace.
    if not (1 <= len(text) <= 200) or not text.strip():
        raise SystemExit("gate failed: entry must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    os.replace(tmp_path, OUTPUT_PATH)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
