**C5 — Data analysis with pandas**

I used **pandas** in **`teen mental health analysis.ipynb`** on **`Teen_Mental_Health_Dataset.csv`** (~1,200 rows of teen self-report: sleep, social media, stress, platform, and related fields). I chose pandas operations to match the questions I actually wanted answered—not to run code for its own sake—and I wrote plain-English comments in each cell stating **what I was asking** and **how to read the output**.

**What I did (operations and why they fit)**

- **`head()` / `info()`** — I asked what a row *means* and whether dtypes and row counts look right before trusting filters or means. That step confirmed one row per teen and which columns are numeric vs categorical, so later steps were not mixing types blindly.

- **`value_counts()`** on **`gender`** and **`platform_usage`** — I asked whether the sample is roughly balanced or dominated by one category. **Male** teens appear slightly more often than **female** (~615 vs ~585), and **Instagram / TikTok / “Both”** are all represented but not identical counts. That matters because any raw difference in averages can partly reflect **who is in the bucket**, not only the behavior we care about.

- **`isnull().sum()`** — I asked how much missing data would weaken row-wise summaries. In this file, missing counts came out **low across columns**, so simple means and filters were reasonable without a heavy missing-data strategy for this exercise.

- **Boolean filter (`stress_level > 6`)** — I asked how many teens land in a **high-stress band** and what **sleep** and **`depression_label`** look like in that slice. About **38%** of rows exceeded the threshold I used, which is a lot: stress is not a rare tail in this dataset, so comparisons to low-stress rows would be worth doing next.

- **`groupby(...).mean()`** — I asked whether **mean sleep** differs by **gender** and whether **mean stress** differs by **main platform**. **Mean sleep** was very close by gender (**about 6.4 vs 6.5 hours**), so gender alone does not show a big sleep gap here. **Mean stress** by platform was also in a **tight band** (roughly **5.3–5.6** on the scale in this file), with **TikTok** slightly **lower** than **“Both”** in my run—**small enough that I would not over-interpret it without checking overlap with age, usage hours, or other columns** (confounding is likely).

**Interpretation (what it means, not just the tables)**

The strongest takeaway for me is the **high-stress slice being large** while **group averages for sleep-by-gender and stress-by-platform stay close**. That pattern suggests the dataset’s variation might be **within** groups (spread, outliers, or other variables) more than between these simple splits—something I noted in the notebook narrative and would **flag for a later milestone** (e.g., controlling for `daily_social_media_hours` or plotting distributions instead of only means).

This work shows I can **load a real table**, pick **appropriate pandas verbs** for each question, and **state what the numbers do and do not imply** for interpretation.
