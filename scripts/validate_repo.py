#!/usr/bin/env python3
"""Small structural check for the teaching repository."""

from pathlib import Path
import csv
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "docs/01-theory.md",
    "docs/04-simulation-guide.md",
    "docs/05-reference-results.md",
    "circuits/ltspice/01-resonant-link.asc",
    "circuits/spice/01-resonant-link.cir",
    "results/reference/ac-sweep-summary.csv",
    "results/figures/ac-sweep-load-power.png",
    "bom/preliminary-bom.csv",
]


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        print("Missing required files:")
        for path in missing:
            print(f"- {path}")
        return 1

    with (ROOT / "results/reference/ac-sweep-summary.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 5:
        print(f"Expected five coupling cases, found {len(rows)}")
        return 1

    print("Repository structure and reference-result summary are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

