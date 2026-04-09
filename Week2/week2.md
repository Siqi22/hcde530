# Week 2 · Competency 2: Code literacy and documentation

Use this file to record **observations** about how you are building *code literacy* (reading, tracing, and reasoning about code) and *documentation* (making work understandable to others and your future self).

Fill in the sections below. The **Interview prompts** at the bottom are questions you can answer here or in conversation; each answer can become a paragraph or bullet under the matching heading.

---

## Summary (one paragraph)

This week we tried generating a data dashboard, running a demo word-count Python script, and writing an app review summary script. Together, those exercises show that we can use Python to sort and analyze data efficiently and get the analysis outputs we need. That is especially useful for UX research when volume grows—interviews, diary studies, surveys, or app reviews—because code can summarize patterns faster than manual sorting alone.

---

## Observations · Code literacy

*What you noticed about understanding and working with code—not only writing it.*

- **Why this matters for research:** Python can turn repetitive counting and summarizing into something repeatable, which scales when you have a lot of qualitative text.
- **Expectations vs. output (`demo_word_count.py`):** Before running the script, I expected to get a word count for each row of text in the CSV. The output confirmed that guess and added summary measures I still needed—shortest, longest, and average word counts—which describe how spread out response lengths are, not only the per-row table.
- **Reading and tracing:** The script felt mostly straightforward: read each row from the CSV, split the response text on whitespace to count words, print a short preview, then compute min/max/average across those counts. No single line felt like a mystery—more like a clear step-by-step path.
- **Data shape and “word” definition:** The demo CSV is one participant per row with columns such as `participant_id`, `role`, and `response`. Each `response` is one long string; we use **`.split()`** (split on whitespace) to break it into chunks and count those chunks as “words.” That is a simple, repeatable rule: anything separated by spaces (or other whitespace) counts. It does **not** strip punctuation—so something like `word,` is still one chunk—or handle empty cells specially; I would spell that out for a teammate so they treat the count as a **length proxy**, not a perfect linguistic word list.
- **Errors and iteration:** *[What broke once? How did you fix it? What did that teach you?]*

---

## Observations · Documentation

*How you (or the sample code) made the work legible to others.*

- **Primary audience:** The professor or TA (for grading) and **future me** (so I can rerun things months later without guessing). Both need a tiny “how to run this” note—not a full engineering README.
- **Naming and structure:** *[Do function and variable names match what they do? Would a teammate understand without asking you?]*
- **Comments and docstrings:** I want a **short note at the top of each script** that says what the file does and **how to run it** when the run path is non-obvious (for example CSV-relative scripts vs. list-only scripts, or a dashboard that needs a local server). The Week 2 Python and HTML files now include that pattern.
- **README or context:** Run Python with **`python3`** (Python 3). From the `Week2` folder (so `demo_responses.csv` is found next to the script): `python3 demo_word_count.py`. From anywhere: `python3 Week2/app_review_summary.py`. For `dashboard.html`, serve the `Week2` folder (for example `python3 -m http.server 8000`) and open `http://localhost:8000/dashboard.html` so the browser can load the CSV.
- **UX angle:** Clear run instructions mirror a good research handoff: someone else can **reproduce** what you did without a live walkthrough—same idea as documenting a session guide or a coded column scheme.

---

## Artifacts (evidence)

*Link or name the files that demonstrate this competency for you.*

| Artifact | What it shows |
|----------|----------------|
| `demo_word_count.py` | Reading structured CSV data, counting words per row, printing a table plus shortest/longest/average summary. |
| `app_review_summary.py` | Working from a list of reviews, counting words each, then summarizing distribution (shortest, longest, average). |
| `dashboard.html` | Loading CSV in the browser, showing KPIs, role breakdown, and keyword-style exploration for communication. |
| `demo_responses.csv` | Example text responses (like research quotes) that the scripts and dashboard consume. |

---

## Growth edge (optional)

*One specific skill you want next—for example: reading error messages, git, CSV edge cases, or explaining a script in two sentences.*

---

## Interview prompts (answer these to fill the sections above)

Answer in your own words; copy useful bits into **Summary** and **Observations** when ready.

1. **This week’s goal:** What did your instructor(or assignment) ask you to demonstrate about data or code—and how did that connect to your UX research or design practice?
   - *Draft answer:* We practiced a dashboard, word counts, and app review summaries to show Python can sort and analyze data and produce the results we need—especially helpful at higher volumes in UX research.
2. **Before vs. after:** Before you ran the scripts, what did you *think* the code did? After running it, what changed in your understanding?
   - *Draft answer (demo word count):* I expected word counts for the CSV text. The run matched that and also surfaced average, shortest, and longest—useful for seeing overall length patterns.
3. **Hardest line or idea:** Name one line, keyword, or concept (for example `DictReader`, `split`, a loop) that was unclear at first. How is it clear to you now?
   - *Draft answer:* Overall it felt straightforward; I could follow the read → count → summarize flow without one part standing out as “hardest.”
4. **Audience:** Who should be able to use your scripts or dashboard without you in the room—classmates, PMs, future you? What did you do to support that?
   - *Draft answer:* Mainly the professor or TA and future me. Running with `python3` is enough if paths and the Week 2 folder layout are documented briefly (this file plus any assignment instructions).
5. **Documentation habit:** What is one documentation habit you want to keep (naming, short comments, a run command, folder structure) after this week?
   - *Draft answer:* A brief top-of-file comment (or docstring) describing purpose and how to run it—especially when there’s a unique way (working directory, local server, etc.).
6. **Integrity of data:** How does your code handle “messy” text (empty lines, long quotes, punctuation)? What would you document for a collaborator about that?
   - *Draft answer:* We use `split()` on the response text, so words are “whatever sits between whitespace.” Punctuation can stay attached; it’s good enough for comparing relative length, but I’d document that assumption for anyone interpreting the numbers.

---

*Last updated: 2026-04-08*
