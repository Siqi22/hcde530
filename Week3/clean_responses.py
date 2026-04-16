"""Clean responses.csv and write responses_clean.csv.

Run from inside Week3:
    python3 clean_responses.py
"""

import csv
from pathlib import Path


def clean_rows(input_path: Path, output_path: Path) -> tuple[int, int]:
    """Remove empty names, uppercase role, and write cleaned rows."""
    kept_rows = 0
    removed_rows = 0

    with input_path.open(newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames or []

        with output_path.open("w", newline="", encoding="utf-8") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                name_value = (row.get("name") or "").strip()
                if not name_value:
                    removed_rows += 1
                    continue

                row["name"] = name_value
                row["role"] = (row.get("role") or "").upper()
                writer.writerow(row)
                kept_rows += 1

    return kept_rows, removed_rows


def main() -> None:
    input_path = Path("responses.csv")
    output_path = Path("responses_clean.csv")

    if not input_path.exists():
        print("Error: responses.csv was not found in the current folder.")
        return

    kept, removed = clean_rows(input_path, output_path)
    print(f"Finished. Wrote {kept} rows to {output_path.name} and removed {removed} rows with empty name.")


if __name__ == "__main__":
    main()
