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
role_counts = {}

for row in rows:
    role = (row.get("role") or "").strip().title()
    if not role:
        continue
    if role in role_counts:
        role_counts[role] += 1
    else:
        role_counts[role] = 1

print("Responses by role:")
for role, count in sorted(role_counts.items()):
    print(f"  {role}: {count}")

# Calculate the average years of experience
total_experience = 0
valid_experience_count = 0

for row in rows:
    raw_experience = (row.get("experience_years") or "").strip()
    try:
        total_experience += int(raw_experience)
        valid_experience_count += 1
    except ValueError:
        continue

if valid_experience_count:
    avg_experience = total_experience / valid_experience_count
    print(f"\nAverage years of experience: {avg_experience:.1f}")
else:
    print("\nAverage years of experience: no valid numeric values")

# Find the top 5 highest satisfaction scores
scored_rows = []
for row in rows:
    raw_score = (row.get("satisfaction_score") or "").strip()
    if not raw_score:
        continue
    try:
        score = int(raw_score)
    except ValueError:
        continue
    participant_name = (row.get("participant_name") or "Unknown").strip()
    scored_rows.append((participant_name, score))

scored_rows.sort(key=lambda x: x[1], reverse=True)
top5 = scored_rows[:5]

print("\nTop 5 satisfaction scores:")
for name, score in top5:
    print(f"  {name}: {score}")
