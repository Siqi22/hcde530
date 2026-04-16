"""Count role frequency in Week2/demo_responses.csv and print to terminal.

Run from repository root:
    python3 Week3/count_demo_roles.py
"""

import csv
from collections import Counter
from pathlib import Path


def count_roles(input_path: Path) -> Counter:
    """Return counts of each role in the input CSV."""
    role_counts: Counter = Counter()

    with input_path.open(newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            role = (row.get("role") or "").strip()
            if role:
                role_counts[role] += 1

    return role_counts


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    input_path = script_dir.parent / "Week2" / "demo_responses.csv"

    if not input_path.exists():
        print("Error: Week2/demo_responses.csv was not found.")
        return

    role_counts = count_roles(input_path)
    total = sum(role_counts.values())

    if total == 0:
        print("No role values found.")
        return

    print("Role counts in demo_responses.csv:")
    for role, count in sorted(role_counts.items(), key=lambda item: (-item[1], item[0])):
        percent = (count / total) * 100
        print(f"  {role:<18} {count:>2} ({percent:>5.1f}%)")

    print(f"\nTotal rows with role values: {total}")


if __name__ == "__main__":
    main()
