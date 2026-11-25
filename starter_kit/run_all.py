"""Build the whole project from the raw data with one command.

    python run_all.py              # data -> checks -> cleaning -> analysis -> graphs -> product page
    python run_all.py --no-render  # the same, but without running Quarto at the end

Each stage reads the previous stage's output and nothing is edited by hand, so anyone
with this folder gets the same results. Keep this file short: the work happens in src/.
EXAMPLE stages below: change the function calls to match your own src/ modules.
"""

import json
import subprocess
import sys

import matplotlib

matplotlib.use("Agg")  # draw figures to files without opening windows

import fetch_data
from src import analyse, clean, config, load_check, visualise


def log(stage: str, rows: int) -> None:
    """Print one line per stage, so a problem shows where it happened."""
    print(f"{stage:<34} {rows:>8,} rows")


def main(render: bool = True) -> None:
    # Stage 2: get the raw data (downloads only what is missing) and read it.
    fetch_data.fetch_all(config.RAW_DIR)
    raw = load_check.read_raw()
    log("read raw file", len(raw))

    # Stage 3: check, then clean. Stop here if a check fails.
    checks = load_check.check_raw(raw)
    config.TABLES_DIR.mkdir(parents=True, exist_ok=True)
    checks.to_csv(config.TABLES_DIR / "checks.csv", index=False)
    load_check.stop_if_failed(checks)
    print(f"{'data checks passed':<34} {len(checks):>8} of {len(checks)}")

    prices = clean.clean(raw)
    config.PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    prices.to_csv(config.PROCESSED_FILE, index=False)
    log("cleaned (one row per date and fuel)", len(prices))

    # Stage 4: analysis tables and headline numbers.
    changes = analyse.weekly_changes(prices)
    frequency = analyse.change_frequency(changes)
    size = analyse.change_size(changes)
    changes.to_csv(config.TABLES_DIR / "weekly_changes.csv", index=False)
    frequency.to_csv(config.TABLES_DIR / "change_frequency.csv")  # the index (year) is part of the table
    size.to_csv(config.TABLES_DIR / "change_size.csv")  # the index (fuel) is part of the table
    log("table weekly_changes", len(changes))
    log("table change_frequency (years)", len(frequency))
    log("table change_size (fuels)", len(size))
    numbers = analyse.headline(prices)
    numbers["correlation"] = analyse.change_correlation(changes, "RON97", "Diesel (Peninsular)")
    (config.TABLES_DIR / "headline.json").write_text(json.dumps(numbers, indent=2) + "\n", encoding="utf-8")

    # Stage 5: graphs, saved as PNG files. The product page draws the same graphs
    # by calling the same functions, so the page and these files always agree.
    figures = {
        "price_trend": visualise.plot_price_trend(prices),
        "change_frequency": visualise.plot_change_frequency(frequency),
        "change_distribution": visualise.plot_change_distribution(changes, "RON97"),
    }
    for name, fig in figures.items():
        visualise.save_figure(fig, config.FIGURES_DIR / f"{name}.png")
    print(f"{'figures saved':<34} {len(figures):>8}")

    # Stage 6: render the dashboard or graph page with Quarto.
    if render:
        page = config.PRODUCT_DIR / config.PRODUCT
        try:
            subprocess.run(["quarto", "render", str(page)], check=True)
        except FileNotFoundError:
            sys.exit("Quarto was not found. Install it from https://quarto.org/docs/get-started/, open a new "
                     "terminal and run again, or use --no-render to skip this step.")
        print(f"Product written to {page.with_suffix('.html')}")


if __name__ == "__main__":
    main(render="--no-render" not in sys.argv)
