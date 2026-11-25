"""The 3AM Fridge Text — writes the one-line fridge text to /output/entry.txt."""

import os

ENTRY = "I put 'Never open me after midnight' on my door. You opened me at 3:04am, stared for 6 minutes, took nothing. Git blame says it was you."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
