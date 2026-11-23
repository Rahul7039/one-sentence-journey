"""One Sentence, One Journey — make.fun entry.

Writes exactly one sentence (a complete journey story) to
/output/entry.txt and prints it. No network, no inputs.
"""

import os

SENTENCE = (
    "She set out from her burned village in nothing but her wedding sari "
    "and her grandmother's iron key, followed the railway line through "
    "fields that smelled of rain and kerosene, and when the key fit no "
    "lock in the new town she melted it into a bell for the school she "
    "built there."
)

OUTPUT_PATH = "/output/entry.txt"


def get_sentence() -> str:
    return SENTENCE


def main() -> None:
    sentence = get_sentence()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(sentence)
    print(sentence)


if __name__ == "__main__":
    main()
