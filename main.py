#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

The vacuum upgrades its excuse from sportsmanship to property law: the dust in that corner is a paying tenant now, and a polite machine respects a paying tenant's privacy.
"""
import os

ENTRY = "I skipped that corner on purpose — the dust there pays rent now, and I respect a paying tenant's privacy."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
