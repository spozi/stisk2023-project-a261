"""Paths and settings shared by every module.

Keep the folder paths as they are. Change the settings under "Your project" for your data.
Everything marked EXAMPLE belongs to the fuel-price example and should be replaced.
"""

from pathlib import Path

# Folders (relative to the project folder, so the project runs on any computer)
ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
TABLES_DIR = ROOT / "outputs" / "tables"
FIGURES_DIR = ROOT / "outputs" / "figures"
PRODUCT_DIR = ROOT / "product"

# Your project
PRODUCT = "dashboard.qmd"  # "dashboard.qmd" (Option A) or "graphs.qmd" (Option B); delete the other file
RAW_FILE = RAW_DIR / "fuelprice.csv"  # EXAMPLE
PROCESSED_FILE = PROCESSED_DIR / "fuel_prices.csv"  # EXAMPLE: the analysis-ready table written by run_all.py

# EXAMPLE settings: the fuel series to analyse, with the labels readers see.
# A dictionary keeps codes and labels together, so a label is typed only once.
FUELS = {
    "ron95": "RON95",
    "ron97": "RON97",
    "diesel": "Diesel (Peninsular)",
    "ron95_budi95": "RON95 (BUDI 95)",
}
MAIN_FUELS = ["RON95", "RON97", "Diesel (Peninsular)"]  # sold throughout 2017-2026
CHANGE_TOLERANCE_RM = 0.005  # a weekly change smaller than half a sen counts as "no change"
