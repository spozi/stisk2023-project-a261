"""Stage 4: compute the numbers and tables that answer your questions.

Owner: <name, role 3>.  Reviewer: <name, role 4>.

Each function takes a DataFrame and returns a new table (or a small dictionary of
headline numbers). Nothing here draws or prints, so every result can be checked and
reused by the graphs and the product page.
EXAMPLE code below: rewrite it for your own data.
"""

import numpy as np
import pandas as pd

from src import config


def weekly_changes(prices: pd.DataFrame) -> pd.DataFrame:
    """One row per fuel and announcement: the change in price since the previous announcement.

    Columns: date, year, fuel, change_sen (whole sen per litre), direction (rise, fall, no change).
    """
    parts = []
    for fuel, group in prices.groupby("fuel", observed=True):  # one fuel at a time
        price = group.sort_values("date")["price_rm"].to_numpy()  # a NumPy array of prices
        change = np.diff(price)  # each price minus the one before it
        direction = np.where(change > config.CHANGE_TOLERANCE_RM, "rise",
                             np.where(change < -config.CHANGE_TOLERANCE_RM, "fall", "no change"))
        parts.append(pd.DataFrame({
            "date": group.sort_values("date")["date"].to_numpy()[1:],  # the first date has no previous price
            "fuel": fuel,
            "change_sen": np.round(change * 100).astype(int),
            "direction": direction,
        }))
    changes = pd.concat(parts, ignore_index=True)
    changes["year"] = changes["date"].dt.year
    changes["fuel"] = pd.Categorical(changes["fuel"], categories=list(config.FUELS.values()), ordered=True)
    return changes[["date", "year", "fuel", "change_sen", "direction"]]


def change_frequency(changes: pd.DataFrame) -> pd.DataFrame:
    """Percentage of announcements in each year at which the price changed (rows: year, columns: fuel).

    A percentage, not a count, because 2017 and the latest year are only part-years.
    """
    changed = changes.assign(changed=changes["direction"] != "no change")
    table = changed.pivot_table(index="year", columns="fuel", values="changed", aggfunc="mean", observed=True)
    return (table * 100).round(1)


def change_size(changes: pd.DataFrame) -> pd.DataFrame:
    """For each fuel, over announcements with a change: how many, the median size, the largest rise and fall."""
    moved = changes[changes["direction"] != "no change"]
    moved = moved.assign(size_sen=moved["change_sen"].abs())
    return moved.groupby("fuel", observed=True).agg(
        changes=("change_sen", "count"),
        median_size_sen=("size_sen", "median"),
        largest_rise_sen=("change_sen", "max"),
        largest_fall_sen=("change_sen", "min"),
    )


def change_correlation(changes: pd.DataFrame, fuel_a: str, fuel_b: str) -> dict:
    """Pearson correlation between two fuels' weekly changes, over the dates both were announced."""
    wide = changes.pivot(index="date", columns="fuel", values="change_sen")
    both = wide[[fuel_a, fuel_b]].dropna()
    r = np.corrcoef(both[fuel_a].to_numpy(), both[fuel_b].to_numpy())[0, 1]
    return {"fuel_a": fuel_a, "fuel_b": fuel_b, "n": int(len(both)), "r": round(float(r), 3)}


def describe_strength(r: float) -> str:
    """Words for the size of a correlation, using a common rule of thumb."""
    size = abs(r)
    if size < 0.3:
        return "weak"
    if size < 0.7:
        return "moderate"
    return "strong"


def headline(prices: pd.DataFrame) -> dict:
    """The key numbers for the value boxes, already formatted as text."""
    latest_date = prices["date"].max()
    numbers = {
        "first_date": f"{prices['date'].min():%d %B %Y}".lstrip("0"),
        "latest_date": f"{latest_date:%d %B %Y}".lstrip("0"),
        "announcements": f"{prices['date'].nunique():,}",
    }
    latest = prices[prices["date"] == latest_date]
    for row in latest.itertuples():
        numbers[row.fuel] = f"RM {row.price_rm:.2f}"
    return numbers
