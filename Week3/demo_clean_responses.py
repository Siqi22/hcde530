"""Clean Week2/demo_responses.csv and write demo_responses_clean.csv.

Run from inside Week3:
    python3 demo_clean_responses.py
"""

import csv
from pathlib import Path
from typing import Tuple


def clean_rows(input_path: Path, output_path: Path) -> Tuple[int, int]:
    """Remove rows with empty participant_id, uppercase role, and write output."""
    kept_rows = 0
    removed_rows = 0

    with input_path.open(newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames or []

        with output_path.open("w", newline="", encoding="utf-8") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                participant_id = (row.get("participant_id") or "").strip()
                if not participant_id:
                    removed_rows += 1
                    continue

                row["participant_id"] = participant_id
                row["role"] = (row.get("role") or "").upper()
                writer.writerow(row)
                kept_rows += 1

    return kept_rows, removed_rows


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    input_path = script_dir.parent / "Week2" / "demo_responses.csv"
    output_path = script_dir / "demo_responses_clean.csv"

    if not input_path.exists():
        print("Error: Week2/demo_responses.csv was not found.")
        return

    kept, removed = clean_rows(input_path, output_path)
    print(
        f"Finished. Wrote {kept} rows to {output_path.name} "
        f"and removed {removed} rows with empty participant_id."
    )


if __name__ == "__main__":
    main()
