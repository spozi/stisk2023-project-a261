# Malaysian pump prices, 2017 to 2026 (EXAMPLE)

> **Starter kit: first steps. Delete this box when you write your own README.**
>
> 1. Install Python 3.11 or newer and [Quarto](https://quarto.org/docs/get-started/) 1.6 or newer, then set up the environment (see "How to run" below).
> 2. Run `python run_all.py`. It builds the worked example, a dashboard of Malaysian fuel prices, and writes `product/dashboard.html`. Open that file in a browser.
> 3. Read the example code in the order it runs: `fetch_data.py` → `src/load_check.py` → `src/clean.py` → `src/analyse.py` → `src/visualise.py` → `product/dashboard.qmd`. Also read `docs/examples/`.
> 4. Make it yours, one stage at a time:
>    - in `fetch_data.py`, replace `SOURCES` with your own data. Delete everything in `data/raw/`, then run `python fetch_data.py`;
>    - in `src/config.py`, set `RAW_FILE`, `PROCESSED_FILE`, `PRODUCT` and your own settings;
>    - rewrite `load_check.py`, `clean.py`, `analyse.py` and `visualise.py` for your data, and update the calls in `run_all.py`;
>    - rewrite `product/dashboard.qmd` or `product/graphs.qmd`, and delete the one you do not use;
>    - fill in the templates in `docs/`, then delete `docs/examples/`.
> 5. Rewrite the "Technical checklist" table below for your own code.
> 6. Before you submit, search the project for the word `EXAMPLE` (VS Code: Ctrl+Shift+F) and remove what is left of the example.

**Team:** EXAMPLE (`<team-id>`: member names, matric numbers and roles are in `docs/proposal.md`)
**For:** a household that sets aside a fixed amount for fuel each month
**Questions:** how often did announced pump prices change each year from 2017 to 2026; how large is a typical change; do RON97 and diesel change together?
**Product:** Option A, a dashboard: `product/dashboard.html` (opens in any browser, no Python needed)

## How to run

From this folder, in a terminal:

```bash
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python run_all.py                    # under a minute; add --no-render to skip Quarto
```

`run_all.py` downloads any missing raw file and checks the saved ones against `data/raw/MANIFEST.json`. It then runs the data checks, cleans the data, writes the tables and graphs in `outputs/`, and renders the product page. It stops with a message if a check fails.

## What is where

```text
fetch_data.py          downloads the raw data and records it in data/raw/MANIFEST.json
run_all.py             runs every stage in order
src/config.py          folders and settings
src/load_check.py      reads the raw data and checks it
src/clean.py           cleaning and reshaping
src/analyse.py         tables and numbers
src/visualise.py       one function per graph
product/               the dashboard (dashboard.qmd) or graph page (graphs.qmd), and the rendered .html
data/raw/              raw files exactly as downloaded (never edited)
data/processed/        the analysis-ready table, written by run_all.py
outputs/               tables (CSV, JSON) and graphs (PNG), written by run_all.py
docs/                  proposal, data card, team contract, decision log, checklists, contributions
```

## Data

| File | Source | Licence | Downloaded |
|---|---|---|---|
| `data/raw/fuelprice.csv` | Price of Petroleum & Diesel, Ministry of Finance, [data.gov.my](https://data.gov.my/data-catalogue/fuelprice) | CC BY 4.0 | 2026-11-25 (see `MANIFEST.json`) |

The data card for this example is `docs/examples/data_card_fuel_prices.md`. Yours goes in `docs/data_card.md`.

## Technical checklist: where our code does each item

Keep this table up to date: at the presentation the lecturer picks two or three rows and asks you to show them.

| Course week | Item | Where (file and function) |
|---|---|---|
| 2 | Functions with docstrings | every file in `src/` |
| 3–4 | NumPy calculation | `src/analyse.py`, `weekly_changes` (`np.diff`, `np.where`) |
| 5 | List or dictionary | `src/config.py`, `FUELS`; `src/load_check.py`, `check_raw` |
| 6 | Select, filter, sort; merge, concat or reshape | `src/clean.py`, `clean` (`melt`); `src/analyse.py`, `weekly_changes` (`concat`) |
| 7 | Category type or table | `src/clean.py`, `clean` (`pd.Categorical`); `src/analyse.py`, `change_frequency` (`pivot_table`) |
| 8 | Loop or `if`; checks that stop the pipeline | `src/analyse.py`, `weekly_changes` (loop); `src/load_check.py`, `stop_if_failed` |
| 9 | Read raw, write processed and outputs | `run_all.py`, `main` |
| 10 | String methods or regular expression | `src/clean.py`, `clean` (`str.strip().str.lower()`); `src/load_check.py`, `check_raw` (date regex) |
| 11 | Descriptive statistics | `src/analyse.py`, `change_size` (median), `change_correlation` (r) |
| 12 | Graphs saved to files | `src/visualise.py`, `plot_*` and `save_figure` |
| 13 | Quarto document running our code | `product/dashboard.qmd` |
| 14 | Self-contained HTML built by `run_all.py` | `product/dashboard.html` (`embed-resources: true`) |

## Extra packages

None beyond `requirements.txt`. If you add one, list it here with a one-sentence reason.
