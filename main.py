#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

The robot vacuum explains why it skipped a spot: it was giving the dust a head start, because fairness matters, even to a vacuum.
"""
import os

ENTRY = "I didn't miss that spot. I was giving the dust a head start. Fairness matters, even to a vacuum."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
