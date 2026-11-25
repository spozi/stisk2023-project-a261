"""Stage 2 and 3a: read the raw data and check it before anything else happens.

Owner: <name, role 1>.  Reviewer: <name, role 2>.

Write one check for every assumption your cleaning and analysis rely on. A check is a
short question about the data with a True or False answer. run_all.py stops if any
check fails, so a problem is caught at the start instead of appearing in a graph.
EXAMPLE code below: rewrite it for your own data.
"""

import numpy as np
import pandas as pd

from src import config

EXPECTED_COLUMNS = ["series_type", "date", "ron95", "ron97", "diesel"]  # EXAMPLE
SERIES_TYPES = ["level", "change_weekly"]  # EXAMPLE: what the column should contain
MAIN_CODES = ["ron95", "ron97", "diesel"]  # EXAMPLE: price columns that must always be filled


def read_raw(path=config.RAW_FILE) -> pd.DataFrame:
    """Read the raw file exactly as downloaded. No cleaning here."""
    return pd.read_csv(path)


def _level_rows(raw: pd.DataFrame) -> pd.DataFrame:
    """The rows holding prices (the file also holds rows of weekly changes)."""
    return raw[raw["series_type"] == "level"]


def _changes_match_prices(raw: pd.DataFrame) -> bool:
    """Does each published weekly change equal this week's price minus last week's?"""
    level = _level_rows(raw).sort_values("date").set_index("date")[MAIN_CODES]
    change = raw[raw["series_type"] == "change_weekly"].set_index("date")[MAIN_CODES]
    if level.index.duplicated().any() or change.index.duplicated().any():
        return False  # cannot be compared; the duplicate check reports the cause
    computed = level.diff().reindex(change.index)
    return bool(np.allclose(computed.to_numpy(), change.to_numpy(), atol=config.CHANGE_TOLERANCE_RM))


def check_raw(raw: pd.DataFrame) -> pd.DataFrame:
    """Run every check and return a table with one row per check: check, passed."""
    missing = [column for column in EXPECTED_COLUMNS if column not in raw.columns]
    if missing:  # without these columns the other checks cannot run
        raise ValueError(f"The raw file is missing these columns: {missing}")

    level = _level_rows(raw)
    checks = {  # description: True when the data are as expected
        "series_type is only 'level' or 'change_weekly'": raw["series_type"].isin(SERIES_TYPES).all(),
        "every date is written YYYY-MM-DD": raw["date"].astype(str).str.fullmatch(r"\d{4}-\d{2}-\d{2}").all(),
        "one row per date and series type": not raw.duplicated(["series_type", "date"]).any(),
        "RON95, RON97 and diesel prices are never missing": level[MAIN_CODES].notna().all().all(),
        "prices are between RM 0.50 and RM 10 per litre": level[MAIN_CODES].stack().between(0.5, 10).all(),
        "published weekly changes equal the change in price": _changes_match_prices(raw),
    }
    return pd.DataFrame({"check": list(checks), "passed": [bool(ok) for ok in checks.values()]})


def stop_if_failed(results: pd.DataFrame) -> None:
    """Raise an error that lists every failed check, so the pipeline stops."""
    failed = results.loc[~results["passed"], "check"].tolist()
    if failed:
        raise ValueError("These data checks failed: " + "; ".join(failed))
