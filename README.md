# Project: Build a Data Science Solution (open title)

**Course:** STISK2023 Programming for Data Science  
**Weight:** 20%  
**Format:** Group project, groups of 5. The team product (90 marks) is shared; 10 marks are awarded to each member individually.  
**Suggested effort:** about 9 hours per student, plus the demonstration  
**Coverage:** Weeks 2–14: Python foundations, NumPy arrays, lists and dictionaries, DataFrames and categories, control flow, input/output, strings and regular expressions, statistics, graphics, reports and publishing  
**Assessed outcome:** **CLO3 (P5, practical skill):** Manipulate data objects using a statistical programming language to identify patterns and relationships.

## Release fields: instructor completes before publication

- **Group registration deadline and link:** `[INSERT]`
- **Checkpoint dates, final submission date/time and LMS link:** `[INSERT]`
- **Demonstration schedule and location:** `[INSERT]`
- **Approved late/special-consideration policy or link:** `[INSERT — do not infer a penalty]`
- **Permitted generative-AI category and disclosure rule:** `[INSERT — e.g., prohibited / limited / permitted with disclosure]`

## What you will do

Your team chooses **its own topic and its own public dataset**, then builds a small data science solution from start to finish. It begins with a question someone actually needs answered and ends with **a dashboard or a page of graphs** that answers it.

There is no fixed dataset and no single correct answer. You are marked on the **process**: how well you choose and document the data, check and clean it, analyse it and show the results. One command must rebuild everything from the raw files.

A **starter kit** gives you the folder structure and a complete worked example (weekly Malaysian fuel prices) to run, read and then replace with your own project.

## The six stages of a data science solution

| Stage | What you do | Where it lives | Weeks |
|---|---|---|---|
| **1. Define** | Name a user and the decision they face; write two or three answerable questions; choose a title | `docs/proposal.md` | 1–2 |
| **2. Acquire** | Find public data with a clear licence; download it with code and record where it came from | `fetch_data.py`, `data/raw/`, `docs/data_card.md` | 9 |
| **3. Check and clean** | Test every assumption about the data; fix problems with code, never by hand; record each decision | `src/load_check.py`, `src/clean.py`, `docs/decision_log.md` | 2–10 |
| **4. Analyse** | Compute the summaries, comparisons and relationships that answer the questions | `src/analyse.py` | 3–7, 11 |
| **5. Visualise** | Draw one clear, honest graph per member | `src/visualise.py` | 12 |
| **6. Deliver** | Build the dashboard or graph page from code and show it working | `product/`, `run_all.py` | 13–14 |

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
3. **Downloadable by code with no login**, so that `fetch_data.py` can get it. A source that needs a login (Kaggle, for example) needs approval at Checkpoint 1, and its original publisher must be traceable.
4. **Big enough to be interesting:** at least 500 rows and 6 columns, including at least 2 numeric columns and at least 1 category or date column. You may combine up to three datasets.
5. **Not already cleaned for teaching.** Classroom datasets (Titanic, Iris, penguins, tips, house-price competitions and similar) are not accepted.
6. **Not a course dataset** as your main data: the Assignment 1 household-income data, the Assignment 2 data and the starter-kit fuel prices may be used only as a second, supporting dataset.
7. **No personal data** about identifiable people (names, IC numbers, phone numbers, home addresses, social-media posts, student or health records). Do not scrape websites or run your own survey.
8. **One team per topic.** Two teams may not use the same main dataset to answer the same questions. Approvals are first come, first served.

### Where to look

- **data.gov.my**: Malaysia's open-data catalogue, <https://data.gov.my/data-catalogue>, and **OpenDOSM**, <https://open.dosm.gov.my>. Each dataset page gives the licence and a direct CSV or parquet link (use that link in `fetch_data.py`). Examples include PriceCatcher item prices, population by state, age and sex, and crime by district.
- **World Bank Open Data**: <https://data.worldbank.org> (development indicators for every country, CC BY 4.0).
- **Our World in Data**: <https://ourworldindata.org> (energy, health, education and more, CC BY, with links to the original sources).

Any other source that meets the rules above is welcome. Check the licence before you write the proposal.

## Your product: a dashboard or a graph page

Choose **one** option in your proposal. Both are built with Quarto from your code (Weeks 13–14) and produce **one HTML file that opens in any browser without Python**.

**Option A: Dashboard** (`product/dashboard.qmd`, Quarto's `dashboard` format)

- two to five **value boxes** with the key numbers (for example the latest value, the largest change, the number of records);
- one **card per graph**, each titled with the question it answers or the finding;
- a short **"What this shows"** card: three to five findings, each with a number;
- an **"About the data"** section or page: source, licence, download date, what one row is, the main limits.

Quarto dashboards extend what you learned in Week 13. The starter kit's example shows every part you need, and the guide is at <https://quarto.org/docs/dashboards/>.

**Option B: Graph page** (`product/graphs.qmd`, Quarto's `html` format)

- the **key numbers** in one or two sentences at the top;
- one **section per graph**, with a heading that states the finding, the graph with a caption and alt text, and two or three sentences with numbers;
- an **"About the data"** section, as in Option A.

**For both options:**

- **One graph or panel per member** (five for a team of five), covering at least **three different kinds**: trend over time, comparison between groups, distribution, relationship between two numeric variables.
- **Every number on the page comes from code**, through Python value boxes or inline expressions (`` `{python} expr` ``). None is typed by hand.
- **Keep the text short:** no more than about 500 words on the page, excluding captions and the "About the data" section. The graphs carry the story.
- Static Matplotlib or Seaborn graphs are expected. Interactive graphs (Plotly, ipywidgets) are optional and earn no extra marks. If you use one, pin the package in `requirements.txt` and give the graph a text summary.

## Technical checklist

Your code, applied to **your own data**, must show each item below at least once, where it does real work. The starter kit shows one example of each. **Each missing item costs 2 marks** in the criterion it belongs to.

| Week | Topic | Show at least one | Where the example does it |
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

You also need **at least six data checks** in `load_check.py` (or your own checks module). Each check is a True/False question about the data, run every time, that stops the pipeline when it fails. For example: are the expected columns present, are there duplicate rows, are the values in a sensible range, are the dates valid?

## Working as a group

Agree on roles at your first meeting and record them in `docs/team_contract.md`. Each member **owns** one stage (writes it), **reviews** another (reads it, runs it and reports problems), and **owns one graph or panel** from end to end: the analysis it needs, the plotting function, its title, caption and alt text, and the sentences about it.

| Role | Owns | Reviews |
|---|---|---|
| **1. Data lead** | Stage 2: finding sources, `fetch_data.py`, the data card | Cleaning |
| **2. Cleaning lead** | Stage 3: the checks and the cleaning code, the decision log | Data card and checks |
| **3. Analysis lead** | Stage 4: `analyse.py` | Graphs |
| **4. Graphs lead** | Stage 5: the shared graph style, `graph_checklist.md` | Analysis |
| **5. Product lead** | Stage 6: the dashboard or graph page, `run_all.py`, `README.md` | That the whole project runs from a fresh copy |

Every member must understand the whole project, not only their own part. At the demonstration anyone may be asked about any part.

**Groups smaller than 5** (only with the instructor's approval): roles are combined, and the team owns one graph per member, but still at least three.

## Checkpoints

| Checkpoint | When | What you submit | What you get back |
|---|---|---|---|
| **C1. Proposal and title approval** | Week 9 | `docs/proposal.md` and `docs/team_contract.md` | **Approved**, **Revise** (resubmit within a week) or **Not approved** |
| **C2. Data ready** | Week 11 | `fetch_data.py` with `MANIFEST.json`, the checks and cleaning running, a draft data card, one draft graph per member | Written feedback on data and graphs |
| **C3. Draft product and peer run** | Week 13 lab | A rendered draft. A member of another team runs your project from your README and fills in `docs/peer_run.md`; you complete `docs/graph_checklist.md` | Peer and instructor comments |
| **Final submission and demonstration** | Week 14 | `PROJECT_<team-id>.zip` (below) and an 8-minute demonstration with 4 minutes of questions | Marks |

Start building only after your proposal is approved. If you later change the main dataset or the questions, get approval again before you continue. Checkpoints carry no separate marks, but C1–C3 are evidence for criteria A and I, and the feedback is there to help you. Record feedback and what you did about it in `docs/decision_log.md`.

**Demonstration:** the product lead shows the question and the user (1 minute). The team runs `python run_all.py` and opens the product. Each member presents their own graph in about one minute: what it shows, why that chart type, and one limitation. Then each member answers one question about any part of the project.

## Starter kit

Download the project repository, <https://github.com/spozi/stisk2023-project-a261> (green **Code** button → **Download ZIP**), unzip it, copy the `starter_kit` folder and rename the copy `PROJECT_<team-id>`. Then:

1. Install Python 3.11 or newer and Quarto 1.6 or newer (<https://quarto.org/docs/get-started/>).
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
└── docs/                  proposal, data card, team contract, decision log, checklists, contributions
                           (docs/examples/ holds the example's proposal and data card)
```

## What to submit

One file, `PROJECT_<team-id>.zip`, containing your project folder after a final `python run_all.py`:

- everything in the tree above, including the **rendered** `product/dashboard.html` (or `graphs.html`);
- `data/raw/` with your raw files and `MANIFEST.json`. If the raw files are larger than 50 MB in total, or the licence does not allow you to share them, leave them out: the marker will run `fetch_data.py`, so it must work;
- `docs/` with the completed proposal, data card, team contract, decision log, graph checklist, peer run, `ai_use.md`, and one `contribution_<matric>.md` per member (250–400 words, written individually).

Delete the starter-kit example before submitting: search the project for the word `EXAMPLE`.

### Rules

- Use Python 3.11 or newer and the packages in `requirements.txt`. Any extra package needs an exact version and a one-sentence reason in the README.
- Use relative paths only (the starter kit's `config.py` does this for you). No `C:\Users\...` or `/Users/...`.
- Never edit data by hand or in Excel. Every change to the data is code that runs in `run_all.py`.
- `python run_all.py` must finish in under 5 minutes on an ordinary laptop. If your data is large, filter it early.
- No passwords, API keys or personal details in any file.

## Marking

### Team product and demonstration: 90 marks

| Criterion | Marks | Full marks look like | Weeks |
|---|---:|---|---|
| **A. Problem and proposal** | 8 | A named user and decision; two or three answerable questions; a clear title; approved at C1 and followed (or changes approved) | 1–2, 13 |
| **B. Data acquisition and documentation** | 12 | Suitable real public data with a recorded licence; `fetch_data.py` reproduces the raw files; a complete, accurate data card | 9 |
| **C. Checking and cleaning** | 20 | At least six checks that stop the pipeline; every cleaning step in code with a reason; text, types, dates and missing values handled honestly; a merge or reshape whose row counts are checked; decisions logged | 2, 5–10 |
| **D. Analysis** | 20 | Summaries that answer each question; at least one comparison between groups and one trend or relationship; statistics that suit the data; NumPy used where it helps; findings stated with their size and their limits, without claiming causes | 3–4, 6–7, 11 |
| **E. Graphs** | 15 | The right chart for each question; honest axes; labels and units; readable; not relying on colour alone; captions and alt text | 12 |
| **F. Product and reproducibility** | 10 | The dashboard or page answers the questions at a glance; every number from code; `python run_all.py` rebuilds everything from the raw data on another computer | 13–14 |
| **G. Team demonstration** | 5 | It runs; the story is clear and on time; every member speaks | 2–14 |
| **Team subtotal** | **90** | | |

### Individual: 10 marks

| Criterion | Marks | Evidence |
|---|---:|---|
| **H. Your graph or panel** | 5 | Its code, chart choice, honesty and accessibility, and how well you explain it at the demonstration |
| **I. Contribution and defence** | 5 | Your stage and review work (checkpoints, decision log, contribution statement) and your answer to one question at the demonstration |
| **Individual subtotal** | **10** | |

**Total: 100 marks, converted to 20% of the course.** There is no hidden peer multiplier. If a member does not contribute, tell the instructor early and record it in the decision log.

## Common problems

| Problem | Fix |
|---|---|
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

- Follow the generative-AI rule in the release fields. Where AI use is allowed, record it in `docs/ai_use.md` (tool, date, purpose, what you used, how you checked it). If no one used it, write "No generative AI was used."
- Cite your data (publisher, link, licence, date) on the product page and in the data card. Cite any code you adapted and any idea you borrowed.
- You may help other teams to understand a tool or an error message. You may not share code, graphs or text with them.
- Never publish anything that identifies a person, and do not name a business or individual in a way that could harm them on the strength of your analysis.
- Each member must be able to explain the team's code and decisions. Work that a member cannot explain may not count towards their individual marks.
