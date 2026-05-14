# Week 6 — C6 Data visualization (competency note)

## What C6 means (in plain language)

C6 is about **making an argument with a chart**, not only drawing a default graph. That means picking a chart type that **matches the shape of the data** (categories vs. time vs. relationships), writing **titles and axis labels** so a reader knows the claim, and publishing a **Jupyter notebook** on GitHub so someone else can **run the code, see the outputs, and read your reasoning** in markdown cells.

---

## What counts as evidence (mapped to this week’s work)

| Requirement | How this week’s work meets it |
|-------------|-------------------------------|
| **At least one chart generated in Python** | There are **three** figures produced from code: **`chart_1.png`**, **`chart_2.png`**, and **`chart_3.png`** in the `Week6/` folder (exports from the analysis notebook). They were built with **`plotly.express`** in Python—the same “grammar of graphics” idea as **matplotlib / seaborn / pandas plotting**, with interactive defaults and clear labels. |
| **Written justification for chart type** | Below, each chart has a **why this chart, not something else** note tied to the **binary grouping** (0 vs 1) and **proportions** being compared. |
| **Notebook on GitHub with code, output, and markdown** | The full reasoning lives in the project notebook (e.g. **`week6_mp1_starter.ipynb`** alongside this folder, or the **`MP1/week6_mp1_starter.ipynb`** copy with Section 4 filled in). **Replace the bracketed link below** with your actual GitHub URL after you push. |

---

## Charts 1–3 (what they show and why that chart type)

### Chart 1 — `chart_1.png`

**What it argues:** Among students with a **social media risk indicator** of **0 vs 1**, **both** self-reported **hopelessness** and **not-good mental health** are **higher** when the indicator is **1** (roughly **~35% vs ~46%** hopelessness and **~23% vs ~33%** not-good mental health in the exported figure).

**Chart type:** **Grouped vertical bar chart** (two colored bar series per x-axis category).

**Why this chart type:** The explanatory question is “**How do two different outcomes compare across two groups?**” A **grouped bar** layout puts **Hopelessness** and **Not good mental health** **side by side** at each level of **Social media (0 vs 1)**, so the reader can compare **both outcomes within a group** and **the same outcome across groups** without implying a false “trend” between 0 and 1 (which a **line** chart can accidentally suggest when x is categorical).

---

### Chart 2 — `chart_2.png`

**What it argues:** **Poor mental health** is **much more common** among students who report **cyberbullying** than among those who do not (roughly **~51% vs ~26%** reporting not-good mental health in the exported figure).

**Chart type:** **Simple vertical bar chart** (one bar per group).

**Why this chart type:** There is **one numeric summary** (a **proportion**) for **two named categories** (“No cyberbullying” vs “Cyberbullying”). A **single bar per category** is the most direct way to show **how large the gap is**—the height **encodes the claim** immediately.

---

### Chart 3 — `chart_3.png`

**What it argues:** Students who report **8 or more hours of sleep** report **hopelessness** **less often** than those **under 8 hours** (roughly **~27% vs ~46%** in the exported figure).

**Chart type:** **Simple vertical bar chart**.

**Why this chart type:** Same structure as Chart 2: **two sleep groups** and **one proportion** (hopelessness). Bars make the **magnitude of the contrast** obvious at a glance and keep the title’s causal-sounding language framed as a **survey pattern** (association), not proof.

---

## competency claim (C6)

> **C6 — Data visualization:** I built **three Python-generated charts** (saved as **`chart_1.png`**, **`chart_2.png`**, and **`chart_3.png`** in my repo’s **`Week6/`** folder) to support **three research questions** about **social media**, **cyberbullying**, and **sleep** in relation to **mental health / hopelessness**. I used **grouped vertical bars** for Chart 1 because I needed to compare **two binary outcomes** side by side across **two social-media groups**—a line would wrongly imply a continuous trend between 0 and 1. I used **simple bar charts** for Charts 2 and 3 because each question compares **one proportion** across **two clear categories** (cyberbullying yes/no; under 8 hours vs 8+ hours sleep). Every chart has a **finding-focused title** and **labeled percent axes** so the argument is readable without decoding variable names.

---
