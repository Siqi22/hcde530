**C5 — Data cleaning and preparation**

This week my cleaning work started from **debugging**, not only from a tidy plan. Messy survey CSVs exposed three concrete failures in my analysis script, and fixing them meant changing both **how I counted** and **what I kept** when building the cleaned file.

**What went wrong and what I had to fix**

- **Role counts included blank roles.** After trimming whitespace, some rows still had an empty `role` string. My first pass still fed those into the counter, which added a misleading “empty” category and skewed the distribution. I changed role counting to **skip rows with no role** so frequency counts only reflect people who actually reported a role, then I still **normalize case** (for example with `.title()`) so “ux researcher” and “UX Researcher” merge for aggregation.

- **Average experience crashed on real input.** I assumed `experience_years` was always numeric text, but the file contained values like **“fifteen”** (a word, not a digit). Calling `int("fifteen")` raises **`ValueError`**, which would stop the whole script. I had to treat parsing as **unsafe by default**: use a `try` / `except ValueError` loop, **only add to the total when conversion succeeds**, and report an average only over valid numbers. The same pattern applies anywhere I turn free text into numbers.

- **The “top 5” satisfaction list did not match the spec.** My first logic did not line up with “highest five **scores**”, it was in reverse order. I fixed it by **collecting only rows with a valid integer `satisfaction_score`**, pairing each score with a name (or `"Unknown"` if the name was blank), **sorting by score from high to low**, and then taking the **first five** entries. That way the list is actually the top five, not the first five rows in file order.

**What I built on top of those fixes**

With those bugs addressed, the **cleaning pipeline** does what the assignment expects: strip fields, drop or skip rows that cannot be analyzed as specified, normalize `role`, require parseable integers for `experience_years` and `satisfaction_score` when writing the cleaned export, and use `"Unknown"` for missing names when I still need the row. I write output to **`week3_survey_cleaned.csv`** and leave the raw messy file unchanged so I can show the before/after and rerun the same steps.

**C3 — Recognizing when code is wrong and why**

The same work supports **C3**: I had to see that a crash, a wrong count, and a wrong “top 5” were **not** random—they came from **types** (string vs int), **empty strings** that look like data, and **order of operations** (filter and sort before slicing). Explaining the fixes in a commit like *“skip blank roles in role counting, fix experience parsing (ValueError, crash at ‘fifteen’), fix top 5 highest logic”* is exactly the kind of record I want, because it names the failure and the idea behind the repair, not only the final architecture.

This work shows I can move from inconsistent, human-entered data to a structured dataset I trust enough to report, because I have already found and fixed the ways it broke my code.
