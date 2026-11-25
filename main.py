"""The Absurd Clause Contest entry.

Writes exactly one original sentence -- a deadpan terms-of-service
clause that quietly turns absurd -- to /output/entry.txt.
Python standard library only.
"""

ENTRY = "You agree that any disputes shall be resolved by a staring contest judged by the office goldfish, whose decision is final and binding."


def main():
    import os
    # Gate mirror: one sentence, 1-200 chars, not only whitespace, no newline.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip() == ENTRY and ENTRY.count(".") == 1
    assert ENTRY.endswith(".")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
