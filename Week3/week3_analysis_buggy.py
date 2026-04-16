import csv

# Load the survey data from a CSV file
filename = "week3_survey_messy.csv"
rows = []

with open(filename, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)


# Count responses by role
# Normalize role names so "ux researcher" and "UX Researcher" are counted together
def count_roles(rows):
    """This method count responses by role"""
    role_counts = {}

    for row in rows:
        role = (row.get("role") or "").strip().title()
        if not role:
            continue
        if role in role_counts:
            role_counts[role] += 1
        else:
            role_counts[role] = 1
    return role_counts

role_counts = count_roles(rows)

print("Responses by role:")
for role, count in sorted(role_counts.items()):
    print(f"  {role}: {count}")

# Calculate the average years of experience
total_experience = 0
valid_experience_count = 0

for row in rows:
    raw = (row.get("experience_years") or "").strip()
    try:
        years = int(raw)
        total_experience += years
        valid_experience_count += 1
    except ValueError:
        continue

if valid_experience_count > 0:
    avg_experience = total_experience / valid_experience_count
    print(f"\nAverage years of experience: {avg_experience:.1f}")
else:
    print("\nAverage years of experience: no valid numeric values")

# Find the top 5 highest satisfaction scores
scored_rows = []
for row in rows:
    raw_score = (row.get("satisfaction_score") or "").strip()
    # if not raw_score:
    #     continue
    try:
        score = int(raw_score)
    except ValueError:
        continue
    participant_name = (row.get("participant_name") or "").strip() or "Unknown"
    scored_rows.append((participant_name, score))

scored_rows.sort(key=lambda x: x[1], reverse=True)
top5 = scored_rows[:5]

print("\nTop 5 satisfaction scores:")
for name, score in top5:
    print(f"  {name}: {score}")


def clean_rows(rows):
    """
    Clean survey data while preserving all original columns.
    - Normalize role to title case
    - Skip rows with blank role
    - Skip rows with invalid experience_years
    - Skip rows with invalid satisfaction_score
    - Fill missing participant_name with "Unknown"
    """
    cleaned = []

    for row in rows:
        cleaned_row = row.copy()

        # Clean participant name
        cleaned_row["participant_name"] = (
            (cleaned_row.get("participant_name") or "").strip() or "Unknown"
        )

        # Clean role
        cleaned_row["role"] = (cleaned_row.get("role") or "").strip().title()
        if not cleaned_row["role"]:
            continue

        # Clean experience_years
        raw_exp = (cleaned_row.get("experience_years") or "").strip()
        try:
            cleaned_row["experience_years"] = int(raw_exp)
        except ValueError:
            continue

        # Clean satisfaction_score
        raw_score = (cleaned_row.get("satisfaction_score") or "").strip()
        try:
            cleaned_row["satisfaction_score"] = int(raw_score)
        except ValueError:
            continue

        cleaned.append(cleaned_row)

    return cleaned


def write_clean_csv(cleaned_rows, output_file):
    """
    Write cleaned survey data to a new CSV file using all columns.
    """
    if not cleaned_rows:
        return

    fieldnames = list(cleaned_rows[0].keys())

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)


def summarize_data(rows):
    """
    Generate a plain-language summary of cleaned survey data.
    """
    row_count = len(rows)

    roles = set()
    empty_names = 0

    for row in rows:
        role = (row.get("role") or "").strip()
        if role:
            roles.add(role)

        name = (row.get("participant_name") or "").strip()
        if not name:
            empty_names += 1

    return (
        f"The cleaned dataset contains {row_count} rows. "
        f"The unique roles are: {', '.join(sorted(roles))}. "
        f"There are {empty_names} rows with empty participant_name fields."
    )


# Load original CSV
filename = "week3_survey_messy.csv"
rows = []

with open(filename, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

# Clean, write, summarize
cleaned_rows = clean_rows(rows)
write_clean_csv(cleaned_rows, "week3_survey_cleaned.csv")

summary = summarize_data(cleaned_rows)
print(summary)