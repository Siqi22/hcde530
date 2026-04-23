"""Search Spoonacular for low-fat pasta recipes and save results to CSV.

Each recipe object is flattened so nested JSON becomes dot-separated columns
(e.g. nutrition.nutrients.0.amount). Uses SPOONACULAR_API_KEY from the repo
root .env file.

API: https://spoonacular.com/food-api/docs#Search-Recipes-Complex

Run from repository root:
    python3 Week4/fetch_spoonacular_pasta_search.py
"""

from __future__ import annotations

import csv
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


# Spoonacular "complex search" endpoint: asks their server for a filtered list of recipes.
# We are not downloading full recipes here—only a short summary per match (see main()).
COMPLEX_SEARCH_URL = "https://api.spoonacular.com/recipes/complexSearch"
OUTPUT_FILENAME = "spoonacular_pasta_search.csv"
ENV_FILENAME = ".env"
ENV_KEY_NAME = "SPOONACULAR_API_KEY"


def load_env(path: Path) -> dict[str, str]:
    """Parse a simple KEY=value .env file (no multiline values)."""

    # Read the local .env file so the API key never lives in source code or git.
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key:
            values[key] = value
    return values


def flatten_to_row(obj: object, prefix: str = "") -> dict[str, str]:
    """Flatten nested dicts/lists into dot-path keys with string leaf values."""

    # Spreadsheets work best with one row per recipe and simple columns. The API often
    # nests data (for example nutrition inside an object). Flattening turns paths like
    # nutrition.nutrients.0.amount into plain column names so you can sort and filter in Excel.
    out: dict[str, str] = {}

    if isinstance(obj, dict):
        if not obj:
            if prefix:
                out[prefix] = "{}"
            return out
        for key, value in obj.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            out.update(flatten_to_row(value, path))
    elif isinstance(obj, list):
        if not obj:
            if prefix:
                out[prefix] = "[]"
            return out
        for index, value in enumerate(obj):
            path = f"{prefix}.{index}"
            out.update(flatten_to_row(value, path))
    else:
        if obj is None:
            out[prefix] = ""
        elif isinstance(obj, bool):
            out[prefix] = "true" if obj else "false"
        else:
            out[prefix] = str(obj)

    return out


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    env_path = repo_root / ENV_FILENAME
    output_path = script_dir / OUTPUT_FILENAME

    # --- API key ---
    env = load_env(env_path)
    api_key = env.get(ENV_KEY_NAME, "").strip()
    if not api_key:
        print(
            f"Error: {ENV_KEY_NAME} was not found or is empty in {env_path}.",
            file=sys.stderr,
        )
        sys.exit(1)

    # --- Build the request URL ---
    # query=pasta          → recipe title/text should match "pasta".
    # maxFat=25            → only recipes with at most 25g fat per serving (Spoonacular applies this filter).
    # number=2             → return at most 2 recipes (keeps the response small for class demos).
    # apiKey=...           → Spoonacular requires your personal key on every call so they can meter usage.
    params = {
        "query": "pasta",
        "maxFat": "25",
        "number": "2",
        "apiKey": api_key,
    }
    url = f"{COMPLEX_SEARCH_URL}?{urllib.parse.urlencode(params)}"

    try:
        # Cloudflare often blocks Python's default urllib User-Agent; use a neutral client string.
        headers = {
            "Accept": "application/json",
            "User-Agent": "HCDE530-coursework/1.0 (recipe search; contact: local student project)",
        }
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        print(f"Error: HTTP {exc.code} from Spoonacular.", file=sys.stderr)
        if detail.strip():
            print(detail, file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as exc:
        print(f"Error: could not reach Spoonacular ({exc.reason}).", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as exc:
        print(f"Error: response was not valid JSON ({exc}).", file=sys.stderr)
        sys.exit(1)

    # --- What came back from the API? ---
    # Spoonacular returns one JSON object with:
    #   - offset, number, totalResults → paging metadata (how many hits exist overall).
    #   - results → a list of short "recipe cards" (not full cooking steps).
    # Each item in results usually includes id, title, image, imageType. When you filter by
    # nutrients (like maxFat), the API can also attach a small nutrition summary so you can
    # see why a recipe matched the filter—we keep whatever fields they send and flatten them.
    results = payload.get("results")
    if not isinstance(results, list):
        print("Error: unexpected response (missing 'results' list).", file=sys.stderr)
        sys.exit(1)

    # --- Turn each recipe into one flat row for the CSV ---
    # We export every field the API gives for each recipe so nothing is dropped silently.
    # Flattening turns nested keys into column names (e.g. nutrition.nutrients.0.name).
    flat_rows: list[dict[str, str]] = []
    for recipe in results:
        if isinstance(recipe, dict):
            flat_rows.append(flatten_to_row(recipe))

    if not flat_rows:
        print("No recipes returned; wrote empty CSV with header only.")
        fieldnames = ["id", "title", "image", "imageType"]
    else:
        # Sort column names so the header row is stable and easy to scan in a spreadsheet.
        fieldnames = sorted({key for row in flat_rows for key in row.keys()})

    try:
        with output_path.open("w", newline="", encoding="utf-8") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            for row in flat_rows:
                writer.writerow({name: row.get(name, "") for name in fieldnames})
    except OSError as exc:
        print(f"Error: could not write {output_path} ({exc}).", file=sys.stderr)
        sys.exit(1)

    total = payload.get("totalResults", "?")
    print(f"Wrote {len(flat_rows)} recipe row(s) to {output_path} (totalResults={total}).")


if __name__ == "__main__":
    main()
