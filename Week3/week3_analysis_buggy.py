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
    Clean survey data:
    - Normalize role names
    - Convert numeric fields
    - Skip rows with invalid numbers
    - Fill missing names
    """
    cleaned = []

    for row in rows:
        # Clean role
        role = (row.get("role") or "").strip().title()
        if not role:
            continue

        # Clean experience
        raw_exp = (row.get("experience_years") or "").strip()
        try:
            experience = int(raw_exp)
        except ValueError:
            continue

        # Clean score
        raw_score = (row.get("satisfaction_score") or "").strip()
        try:
            score = int(raw_score)
        except ValueError:
            continue

        # Clean name
        name = (row.get("participant_name") or "").strip() or "Unknown"

        cleaned.append({
            "participant_name": name,
            "role": role,
            "experience_years": experience,
            "satisfaction_score": score
        })

    return cleaned


def write_clean_csv(cleaned_rows, output_file):
    """
    Write cleaned survey data to a new CSV file.
    """
    fieldnames = ["participant_name", "role", "experience_years", "satisfaction_score"]

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)

cleaned_rows = clean_rows(rows)
write_clean_csv(cleaned_rows, "week3_survey_cleaned.csv")