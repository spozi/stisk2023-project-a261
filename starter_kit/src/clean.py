"""Stage 3b: turn the checked raw data into one tidy, analysis-ready table.

Owner: <name, role 2>.  Reviewer: <name, role 1>.

Rules for this file:
- start from a copy of the raw DataFrame and never change the raw file;
- write each cleaning decision as code, with a comment saying why, and record it in
  docs/decision_log.md;
- keep a value missing (NaN) when it is unknown. Never replace it with 0.
EXAMPLE code below: rewrite it for your own data.
"""

import pandas as pd

from src import config


def clean(raw: pd.DataFrame) -> pd.DataFrame:
    """Return one row per announcement date and fuel, with columns date, year, fuel, price_rm."""
    df = raw.copy()

    # Text tidying: column names and labels in one consistent form ("Level " -> "level").
    df.columns = df.columns.str.strip().str.lower()
    df["series_type"] = df["series_type"].str.strip().str.lower()

    # Keep the price rows. The weekly-change rows repeat the same information, and
    # load_check.py has already confirmed that they agree with the prices.
    prices = df[df["series_type"] == "level"].copy()
    prices["date"] = pd.to_datetime(prices["date"], format="%Y-%m-%d")

    # Reshape from wide (one column per fuel) to long (one row per fuel and date),
    # the shape that grouping and Seaborn both expect.
    long = prices.melt(
        id_vars="date", value_vars=list(config.FUELS), var_name="fuel_code", value_name="price_rm"
    )
    # Row-count check: a reshape must give exactly one row per date and fuel.
    if len(long) != len(prices) * len(config.FUELS):
        raise ValueError(f"reshape gave {len(long)} rows, expected {len(prices) * len(config.FUELS)}")

    # A series is empty before it began (BUDI 95 started on 30 September 2025). Those rows
    # are "not applicable", not zero, so they are removed rather than filled in.
    long = long.dropna(subset=["price_rm"])

    # Readable labels as an ordered category, so tables and legends keep the same order.
    long["fuel"] = pd.Categorical(
        long["fuel_code"].map(config.FUELS), categories=list(config.FUELS.values()), ordered=True
    )
    long["year"] = long["date"].dt.year
    return long[["date", "year", "fuel", "price_rm"]].sort_values(["fuel", "date"]).reset_index(drop=True)


def read_processed(path=config.PROCESSED_FILE) -> pd.DataFrame:
    """Read the processed CSV back with the same types that clean() produced."""
    df = pd.read_csv(path, parse_dates=["date"])
    df["fuel"] = pd.Categorical(df["fuel"], categories=list(config.FUELS.values()), ordered=True)
    return df
