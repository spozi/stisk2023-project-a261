# Project: Build a Data Science Solution (open title)

**Course:** STISK2023 Programming for Data Science  
**Weight:** 20%  
**Format:** Group project, groups of 5. The team product (90 marks) is shared; 10 marks are awarded to each member individually.  
**Duration:** 3 weeks from release to final submission  
**Suggested effort:** about 9 hours per student (about 3 hours a week), plus the final presentation  
**Coverage:** Course weeks 2–14: Python foundations, NumPy arrays, lists and dictionaries, DataFrames and categories, control flow, input/output, strings and regular expressions, statistics, graphics, reports and publishing  
**Assessed outcome:** **CLO3 (P5, practical skill):** Manipulate data objects using a statistical programming language to identify patterns and relationships.

## What you will do

Your team chooses **its own topic and its own public dataset**, then builds a small data science solution from start to finish. It begins with a question someone actually needs answered and ends with **a dashboard or a page of graphs** that answers it.

There is no fixed dataset and no single correct answer. You are marked on the **process**: how well you choose and document the data, check and clean it, analyse it and show the results. One command must rebuild everything from the raw files.

**All marks are awarded at a 15-minute presentation to the lecturer** at the end of week 3. There you walk through your solution, run it live, and each member presents and defends their own graph (see "Final presentation" below).

You have **three weeks**, so keep the project small: **one dataset, two questions, one graph per member**. A small project done carefully scores higher than an ambitious one left half-finished. The **starter kit** already does most of the plumbing: it has the folder structure and a complete worked example (weekly Malaysian fuel prices) that you run, read and then replace with your own data.

## The six stages of a data science solution

| Stage | What you do | Where it lives | Course weeks |
|---|---|---|---|
| **1. Define** | Name a user and the decision they face; write two answerable questions; choose a title | `docs/proposal.md` | 1–2 |
| **2. Acquire** | Find public data with a clear licence; download it with code and record where it came from | `fetch_data.py`, `data/raw/`, `docs/data_card.md` | 9 |
| **3. Check and clean** | Test your assumptions about the data; fix problems with code, never by hand; record each decision | `src/load_check.py`, `src/clean.py`, `docs/decision_log.md` | 2–10 |
| **4. Analyse** | Compute the summaries, comparisons and relationships that answer the questions | `src/analyse.py` | 3–7, 11 |
| **5. Visualise** | Draw one clear, honest graph per member | `src/visualise.py` | 12 |
| **6. Deliver** | Build the dashboard or graph page from code and show it working | `product/`, `run_all.py` | 13–14 |

## Three-week plan

| When | Team goal | Checkpoint |
|---|---|---|
| **Week 1, days 1–2** | Form the team and agree roles. Everyone runs the starter-kit example. Choose a topic, find a dataset, **download it and open it in pandas** before proposing it | |
| **Week 1, day 3** | Submit the proposal | **C1** |
| **Week 1, days 4–7** | Point `fetch_data.py` at your data; write the checks and the cleaning; get `run_all.py` running end to end with your data, even if the page shows a single rough graph | **C2** at the end of the week |
| **Week 2** | Analysis tables; each member draws their graph; first rendered draft of the dashboard or graph page; data card | **C3** at the end of the week (peer run in the lab) |
| **Week 3** | Fix what the peer run found; finish titles, captions and alt text; remove the example; fill in the checklist table in the README; contribution statements; rehearse the presentation; submit | **Final submission and presentation** at the end of the week |

Get the whole pipeline running with your own data **in week 1**, however rough. It is much easier to improve a working project than to join five unfinished pieces in week 3.

## Choosing your title and data

### A good question

A good project question is about something real, names who it is for, and can be answered with data. It asks **what, where, when, how much or how often**, never **why**: data like yours can show patterns, not causes.

| Weak | Better |
|---|---|
| "Analysis of crime in Malaysia" (no question, no user) | "Which districts had the largest fall in property crime between 2017 and 2023? For a family choosing where to rent." |
| "Why are food prices rising?" (asks for a cause) | "Which essential items rose most in price over the last year, and in which states? For a student budgeting their monthly groceries." |
| "Is Malaysia developing?" (too vague to answer) | "How has electricity use per person changed in ASEAN countries since 2000, and is it higher where incomes are higher? For a policy student." |

The questions above are **ideas only**. Your proposal must be your own and must be approved.

### Rules for the data

1. **Real and public**, published by an identifiable organisation (a government agency, an international body, a research group). Malaysian data is encouraged.
2. **Licensed for reuse**, for example CC BY 4.0 or an open-government licence, or published under terms that allow educational use. Record the licence in your data card.
3. **Downloadable by code with no login**, so that `fetch_data.py` can get it. Sources that need a login (Kaggle, for example) are not accepted: there is no time to sort out exceptions.
4. **The right size for three weeks:** at least 500 rows and 6 columns, including at least 2 numeric columns and at least 1 category or date column, and small enough to download and process in a few minutes (as a guide, under 100 MB). Use **one main dataset**. You may add one small second dataset (for example population, to compare per person), but you do not have to.
5. **Not already cleaned for teaching.** Classroom datasets (Titanic, Iris, penguins, tips, house-price competitions and similar) are not accepted.
6. **Not a course dataset** as your main data: the Assignment 1 household-income data, the Assignment 2 data and the starter-kit fuel prices may be used only as the second, supporting dataset.
7. **No personal data** about identifiable people (names, IC numbers, phone numbers, home addresses, social-media posts, student or health records). Do not scrape websites or run your own survey.
8. **One team per topic.** Two teams may not use the same main dataset to answer the same questions. Approvals are first come, first served, so propose early.

### Where to look

- **data.gov.my**: Malaysia's open-data catalogue, <https://data.gov.my/data-catalogue>, and **OpenDOSM**, <https://open.dosm.gov.my>. Each dataset page gives the licence and a direct CSV or parquet link (use that link in `fetch_data.py`). Examples include PriceCatcher item prices, population by state, age and sex, and crime by district. **This is the fastest route:** the data is clean enough to start quickly but still needs checking, and the licence is clear.
- **World Bank Open Data**: <https://data.worldbank.org> (development indicators for every country, CC BY 4.0).
- **Our World in Data**: <https://ourworldindata.org> (energy, health, education and more, CC BY, with links to the original sources).

Any other source that meets the rules above is welcome. Check the licence, and that the download link works, before you write the proposal.

## Your product: a dashboard or a graph page

Choose **one** option in your proposal. Both are built with Quarto from your code (course weeks 13–14) and produce **one HTML file that opens in any browser without Python**. The starter kit has a working template for each, so you adapt one rather than starting from a blank file.

**Option A: Dashboard** (`product/dashboard.qmd`, Quarto's `dashboard` format)

- two to five **value boxes** with the key numbers (for example the latest value, the largest change, the number of records);
- one **card per graph**, each titled with the question it answers or the finding;
- a short **"What this shows"** card: three to five findings, each with a number;
- an **"About the data"** section or page: source, licence, download date, what one row is, the main limits.

Quarto dashboards extend what you learned in course week 13. The starter kit's example shows every part you need, and the guide is at <https://quarto.org/docs/dashboards/>.

**Option B: Graph page** (`product/graphs.qmd`, Quarto's `html` format)

- the **key numbers** in one or two sentences at the top;
- one **section per graph**, with a heading that states the finding, the graph with a caption and alt text, and one or two sentences with numbers;
- an **"About the data"** section, as in Option A.

If your team is unsure, choose **Option B**: it uses only what you learned in course week 13.

**For both options:**

- **One graph or panel per member** (five for a team of five), covering at least **three different kinds**: trend over time, comparison between groups, distribution, relationship between two numeric variables.
- **Every number on the page comes from code**, through Python value boxes or inline expressions (`` `{python} expr` ``). None is typed by hand.
- **Keep the text short:** about 300 words on the page, excluding captions and the "About the data" section. The graphs carry the story.
- Static Matplotlib or Seaborn graphs are expected. Interactive graphs (Plotly, ipywidgets) are optional and earn no extra marks.

## Technical checklist

Your code, applied to **your own data**, must show each item below at least once, where it does real work. Most of them appear naturally once you adapt the starter kit; the last column shows where the example does each one. **Each missing item costs 1 mark** in the criterion it belongs to.

| Course week | Topic | Show at least one | Where the example does it |
|---|---|---|---|
| 2 | Python basics | Functions with docstrings, each doing one job | every file in `src/` |
| 3–4 | NumPy | A calculation on a NumPy array (`np.diff`, `np.where`, `np.percentile`, array arithmetic) | `analyse.weekly_changes` |
| 5 | Lists and dictionaries | A list or dictionary that holds settings, labels or results | `config.FUELS`, `load_check.check_raw` |
| 6 | DataFrames | Selecting, filtering and sorting, plus a merge, concat or reshape (`melt`, `pivot`) | `clean.clean` |
| 7 | Factors and tables | A category type, or `value_counts`, `crosstab`, `pivot_table` or `pd.cut` | `clean.clean`, `analyse.change_frequency` |
| 8 | Control statements | A loop or `if` that is needed, and data checks that stop the pipeline when they fail | `analyse.weekly_changes`, `load_check.stop_if_failed` |
| 9 | Input and output | Reading the raw files, and writing the processed CSV and output tables | `run_all.py` |
| 10 | Strings | String methods or a regular expression on a text column | `clean.clean`, `load_check.check_raw` |
| 11 | Statistics | Descriptive statistics that suit the data (median, percentage, spread, correlation) | `analyse.change_size`, `analyse.change_correlation` |
| 12 | Graphics | Matplotlib or Seaborn graphs, saved to files | `src/visualise.py` |
| 13 | Reports | A Quarto document that runs your code | `product/*.qmd` |
| 14 | Publishing | A self-contained HTML page built by `run_all.py` | `product/dashboard.html` |

Copy this table into your `README.md` and replace the last column with **where your own code does it** (file and function). At the presentation the lecturer will pick two or three items and ask you to show them; an item you cannot show counts as missing.

You also need **at least five data checks** in `load_check.py`. Each check is a True/False question about the data, run every time, that stops the pipeline when it fails. For example: are the expected columns present, are there duplicate rows, are the values in a sensible range, are the dates valid? Most checks are one line each.

## Working as a group

Agree on roles at your first meeting and record them in the proposal. Each member **owns** one stage (writes it), **reviews** another (reads it, runs it and reports problems), and **owns one graph or panel** from end to end: the analysis it needs, the plotting function, its title, caption and alt text, and the sentences about it.

| Role | Owns | Reviews |
|---|---|---|
| **1. Data lead** | Stage 2: finding the data, `fetch_data.py`, the data card | Cleaning |
| **2. Cleaning lead** | Stage 3: the checks and the cleaning code, the decision log | Data card and checks |
| **3. Analysis lead** | Stage 4: `analyse.py` | Graphs |
| **4. Graphs lead** | Stage 5: the shared graph style, `graph_checklist.md` | Analysis |
| **5. Product lead** | Stage 6: the dashboard or graph page, `run_all.py`, `README.md` | That the whole project runs from a fresh copy |

Stages overlap in three weeks, so work in parallel. While the data and cleaning leads get the data in, the others can adapt the example's graph and page code using the example data, then switch to the team's data when it is ready.

Every member must understand the whole project, not only their own part. At the presentation anyone may be asked about any part.

**Groups smaller than 5** (only with the instructor's approval): roles are combined, and the team owns one graph per member, but still at least three.

## Checkpoints

| Checkpoint | When | What you submit | What you get back |
|---|---|---|---|
| **C1. Proposal and title approval** | Week 1, day 3 | `docs/proposal.md`, including roles | **Approved**, **Revise** (resubmit within two days) or **Not approved**, within two working days |
| **C2. Data ready** | End of week 1 | `fetch_data.py` with `MANIFEST.json`, at least five checks and the cleaning running in `run_all.py` | Short written feedback |
| **C3. Draft product and peer run** | End of week 2 (lab) | A rendered draft with one graph per member. A member of another team runs your project from your README and fills in `docs/peer_run.md` (about 15 minutes) | Peer and instructor comments |
| **Final submission and presentation** | End of week 3 | `PROJECT_<team-id>.zip` (below), submitted before your slot, and a 15-minute presentation to the lecturer | Marks, at the presentation |

You do not need to wait for approval to start: download your data and run checks while you wait. If you are asked to revise, usually only the questions change. If you later change the main dataset or the questions, get approval again before you continue. Checkpoints carry no separate marks, but C1–C3 are evidence for criteria A and I. Record feedback and what you did about it in `docs/decision_log.md`.

## Final presentation

**15 minutes per team: 10 minutes presenting, 5 minutes of questions.** No slides: present from your dashboard or graph page, your code and your `docs/` on one laptop, with the project folder open in your editor and the product open in a browser. Every member must attend and speak. Marks are decided at the presentation, from what you show and how you answer.

| Part | Time | Who | What to show | Criteria |
|---|---|---|---|---|
| 1. Problem | 1 min | Product lead | The user, their decision, the two questions, and the answer in one sentence | A |
| 2. Data | 1½ min | Data lead | Where the data comes from and its licence (`fetch_data.py`, `MANIFEST.json`), what one row is, and one limit from the data card | B |
| 3. Checks and cleaning | 1½ min | Cleaning lead | The checks in `load_check.py` and the two most important cleaning decisions, with how many rows each affected (decision log) | C |
| 4. Live run | 1 min | Product lead | Run `python run_all.py` and reopen the product. Start it at the beginning of part 2, so it finishes while you talk | F |
| 5. Graphs | 5 min | Every member, about 1 min each | Your own graph: the question it answers, what it shows (with the number), why that chart type, and one limitation | D, E, H |
| 6. Questions | 5 min | Lecturer | One question to each member, about any part of the project. The lecturer may also ask you to show two or three items from your checklist table | I, checklist |

Rehearse once with a timer: you will be stopped at 10 minutes. If `run_all.py` fails on the day, do not debug it in front of the lecturer: open the outputs from your last successful run and explain what went wrong (this costs marks in F only).

## Starter kit

Download the project repository, <https://github.com/spozi/stisk2023-project-a261> (green **Code** button → **Download ZIP**), unzip it, copy the `starter_kit` folder and rename the copy `PROJECT_<team-id>`. Then:

1. Install Python 3.11 or newer and Quarto 1.6 or newer (<https://quarto.org/docs/get-started/>). Do this on day 1: installation problems are the most common cause of a slow start.
2. In the project folder, create an environment and install the packages:

   ```bash
   python -m venv .venv
   source .venv/bin/activate          # Windows: .venv\Scripts\activate
   python -m pip install -r requirements.txt
   ```

3. Run `python run_all.py` and open `product/dashboard.html`. This is the worked example: a dashboard of weekly fuel prices.
4. Read the example in the order it runs, then follow the "first steps" in the starter kit's README to replace it with your own project, one stage at a time.

```text
PROJECT_<team-id>/
├── README.md              how to run your project (replace the example)
├── requirements.txt       exact package versions
├── fetch_data.py          downloads raw data; you edit SOURCES only
├── run_all.py             runs every stage in order
├── src/                   config.py, load_check.py, clean.py, analyse.py, visualise.py
├── product/               dashboard.qmd (Option A) or graphs.qmd (Option B)
├── data/raw/              raw files and MANIFEST.json, never edited
├── data/processed/        written by run_all.py
├── outputs/               tables and graphs, written by run_all.py
└── docs/                  proposal, data card, decision log, checklists, contributions
                           (docs/examples/ holds the example's proposal and data card)
```

## What to submit

One file, `PROJECT_<team-id>.zip`, containing your project folder after a final `python run_all.py`:

- everything in the tree above, including the **rendered** `product/dashboard.html` (or `graphs.html`);
- `data/raw/` with your raw files and `MANIFEST.json`. If the raw files are larger than 50 MB in total, leave them out: the marker will run `fetch_data.py`, so it must work;
- `README.md` including your completed technical-checklist table (file and function for each item);
- `docs/` with:
  - `proposal.md` (as approved, plus any approved changes);
  - `data_card.md` (about one page);
  - `decision_log.md`;
  - `graph_checklist.md`;
  - `peer_run.md`;
  - `ai_use.md`;
  - one `contribution_<matric>.md` per member (150–250 words, written individually).

`team_contract.md` in the starter kit is optional: use it if it helps your team.

Delete the starter-kit example before submitting: search the project for the word `EXAMPLE`.

### Rules

- Use Python 3.11 or newer and the packages in `requirements.txt`. Any extra package needs an exact version and a one-sentence reason in the README.
- Use relative paths only (the starter kit's `config.py` does this for you). No `C:\Users\...` or `/Users/...`.
- Never edit data by hand or in Excel. Every change to the data is code that runs in `run_all.py`.
- `python run_all.py` must finish in under 5 minutes on an ordinary laptop. If your data is large, filter it early.
- No passwords, API keys or personal details in any file.

## Marking

**All marks are given at the final presentation**, from what your team shows and how each member answers. The lecturer has your submitted zip open as a record, so what you show must match what you submitted. Marks reward a careful project of the size this brief asks for: two questions, one dataset, one graph per member. Extra questions, datasets or features earn no extra marks.

### Team product and presentation: 90 marks

| Criterion | Marks | Full marks look like | Course weeks |
|---|---:|---|---|
| **A. Problem and proposal** | 8 | A named user and decision; two answerable questions; a clear title; approved at C1 and followed (or changes approved) | 1–2, 13 |
| **B. Data acquisition and documentation** | 12 | Suitable real public data with a recorded licence; `fetch_data.py` reproduces the raw files; a short, accurate data card | 9 |
| **C. Checking and cleaning** | 20 | At least five checks that stop the pipeline; every cleaning step in code with a reason; text, types, dates and missing values handled honestly; a merge or reshape whose row counts are checked; decisions logged | 2, 5–10 |
| **D. Analysis** | 20 | Summaries that answer both questions; at least one comparison between groups and one trend or relationship; statistics that suit the data; NumPy used where it helps; findings stated with their size and their limits, without claiming causes | 3–4, 6–7, 11 |
| **E. Graphs** | 15 | The right chart for each question; honest axes; labels and units; readable; not relying on colour alone; captions and alt text | 12 |
| **F. Product and reproducibility** | 10 | The dashboard or page answers the questions at a glance; every number from code; `python run_all.py` rebuilds everything from the raw data, live | 13–14 |
| **G. Presentation** | 5 | Clear, in order and within 10 minutes; every member speaks; the answer to both questions is obvious by the end | 2–14 |
| **Team subtotal** | **90** | | |

### Individual: 10 marks

| Criterion | Marks | Evidence |
|---|---:|---|
| **H. Your graph or panel** | 5 | Its code, chart choice, honesty and accessibility, and how well you present it (part 5) |
| **I. Contribution and defence** | 5 | Your answer to your question in part 6, supported by your stage and review work (checkpoints, decision log, contribution statement) |
| **Individual subtotal** | **10** | |

**Total: 100 marks, converted to 20% of the course.** There is no hidden peer multiplier. If a member does not contribute, tell the instructor early and record it in the decision log.

## Common problems

| Problem | Fix |
|---|---|
| Running out of time | Cut scope, not care: drop a question part or the second dataset, not the checks or the captions. Make sure `run_all.py` works from start to end before polishing anything. |
| `quarto: command not found` | Install Quarto, then open a **new** terminal. Meanwhile, `python run_all.py --no-render` runs everything else. |
| Quarto cannot find a `python3` Jupyter kernel | Activate your environment and run `python -m pip install -r requirements.txt` again (it installs Jupyter); `quarto check jupyter` shows what Quarto sees. |
| `ModuleNotFoundError: No module named 'src'` when rendering | Keep the `sys.path.insert(...)` line in the page's first cell, and keep the `.qmd` file in `product/`. |
| A value box is empty or the render fails at a value box | The value must be text: `value=f"{x:.2f}"`, not a NumPy number. |
| A graph appears twice | End the cell with `fig = ...` (an assignment), not the bare function call. |
| The page shows `np.float64(3.72)` | Format numbers with f-strings in inline expressions: `` `{python} f"{x:.2f}"` ``. |
| `ValueError: assignment destination is read-only` | pandas 3 can return a read-only array. Use `df["col"].to_numpy(copy=True)` before changing it. |
| The download link does not work in `fetch_data.py` | Open the link in a browser first. On data.gov.my, copy the direct CSV or parquet link from the dataset page, not the page address. |
| `run_all.py` is slow or runs out of memory | Read only the columns you need (`usecols=`), filter rows early, and prefer parquet files for large data. |

## Integrity, privacy and attribution

- Follow the generative-AI rule announced by the lecturer. Where AI use is allowed, record it in `docs/ai_use.md` (tool, date, purpose, what you used, how you checked it). If no one used it, write "No generative AI was used."
- Cite your data (publisher, link, licence, date) on the product page and in the data card. Cite any code you adapted and any idea you borrowed.
- You may help other teams to understand a tool or an error message. You may not share code, graphs or text with them.
- Never publish anything that identifies a person, and do not name a business or individual in a way that could harm them on the strength of your analysis.
- Each member must be able to explain the team's code and decisions. Work that a member cannot explain may not count towards their individual marks.
