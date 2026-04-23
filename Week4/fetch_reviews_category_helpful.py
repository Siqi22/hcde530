"""Fetch app reviews from the HCDE 530 Week 4 API and save category + helpful votes to CSV.

API docs: https://brockcraft.github.io/docs/hcde530_api_documentation.html

Run from repository root:
    python3 Week4/fetch_reviews_category_helpful.py

Or from Week4:
    python3 fetch_reviews_category_helpful.py

If Python reports an SSL certificate error on macOS, run the
"Install Certificates.command" helper that ships with your Python install.
"""

import csv
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


API_BASE = "https://hcde530-week4-api.onrender.com"
REVIEWS_PATH = "/reviews"
DEFAULT_LIMIT = 10
OUTPUT_FILENAME = "reviews_category_helpful.csv"


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    output_path = script_dir / OUTPUT_FILENAME

    query = urllib.parse.urlencode({"limit": str(DEFAULT_LIMIT), "offset": "0"})
    url = f"{API_BASE.rstrip('/')}{REVIEWS_PATH}?{query}"

    try:
        request = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        print(f"Error: HTTP {exc.code} while calling the API.", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as exc:
        print(f"Error: could not reach the API ({exc.reason}).", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as exc:
        print(f"Error: response was not valid JSON ({exc}).", file=sys.stderr)
        sys.exit(1)

    reviews = payload.get("reviews") or []
    if not reviews:
        print("No reviews returned.")
        return

    rows: list[tuple[str, int]] = []
    print("Category (research) | Helpful votes")
    print("-" * 40)
    for item in reviews:
        category = (item.get("category") or "").strip()
        helpful = item.get("helpful_votes")
        if helpful is None:
            helpful = 0
        try:
            helpful_int = int(helpful)
        except (TypeError, ValueError):
            helpful_int = 0
        rows.append((category, helpful_int))
        print(f"{category} | {helpful_int}")

    try:
        with output_path.open("w", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["category", "helpful_votes"])
            writer.writerows(rows)
    except OSError as exc:
        print(f"Error: could not write {output_path} ({exc}).", file=sys.stderr)
        sys.exit(1)

    print(f"\nSaved {len(rows)} row(s) to {output_path}")


if __name__ == "__main__":
    main()
