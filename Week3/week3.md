**C5 — Data cleaning and preparation**

I built a small cleaning pipeline that turns messy survey-style CSVs into something I can analyze without silent errors. I normalize categorical text (especially `role`) so variants like “ux researcher” and “UX Researcher” are treated as one category when I count or aggregate. I strip whitespace on identifiers and names, drop rows that cannot represent a real participant (for example empty `name` or `participant_id`), and—where I still need the row for analysis—I fill missing `participant_name` with `"Unknown"` so downstream code always has a string to work with. For numeric fields such as `experience_years` and `satisfaction_score`, I parse safely and skip values that are not valid integers so averages and rankings are not distorted by typos or blanks. I write cleaned results to **new** CSV files and keep the raw inputs unchanged, which preserves a clear audit trail and lets me rerun the same steps on updated data.

**Rationale for these choices**

- **Normalize roles (case and spacing)** so frequency counts and charts reflect real role groups instead of accidental duplicates from typing or capitalization.
- **Remove rows with empty IDs or names** because they cannot be tied to a person; keeping them would inflate counts or break joins between tables.
- **Validate numbers before averaging or ranking** so summary statistics stay trustworthy; invalid cells are common in “messy” exports and should not silently become zeros.
- **Use `"Unknown"` only where dropping the row would lose other useful columns** so I can still report on satisfaction or experience while being explicit about missing identity fields.
- **Write outputs to new files** so I never overwrite the original capture, which supports reproducibility and makes it obvious which file is “raw” versus “clean.”

This work shows I can move from inconsistent, human-entered data to a structured dataset that supports reliable analysis in later steps.
