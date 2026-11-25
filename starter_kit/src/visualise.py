"""Stage 5: graphs. Each function takes a table and returns a Matplotlib Figure.

Every member owns one graph function: write your name on it. save_figure is shared.
A figure has axis labels and units but no title: the title, which states the finding,
goes on the dashboard card or the graph page, where it can be checked against the numbers.
EXAMPLE code below: rewrite it for your own data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from src import config

sns.set_theme(style="whitegrid", palette="colorblind")

# One colour and one line style per fuel, used in every graph, so a reader learns them once.
# Line styles mean the graphs can still be read without colour.
COLOURS = dict(zip(config.FUELS.values(), sns.color_palette("colorblind", len(config.FUELS))))
LINE_STYLES = dict(zip(config.FUELS.values(), ["-", "--", "-.", ":"]))
HATCHES = ["", "//", ".."]


def save_figure(fig: plt.Figure, path: Path, dpi: int = 200) -> Path:
    """Save fig as a PNG (at least 150 dpi), create the folder if needed, and close the figure."""
    if dpi < 150:
        raise ValueError("save figures at 150 dpi or more so they stay sharp")
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)
    return path


def plot_price_trend(prices: pd.DataFrame) -> plt.Figure:
    """Trend (owner: <name>): price per litre of each fuel at every announcement."""
    fig, ax = plt.subplots(figsize=(10, 4))
    for fuel, group in prices.groupby("fuel", observed=True):
        ax.plot(group["date"], group["price_rm"], drawstyle="steps-post",  # a price holds until the next announcement
                color=COLOURS[fuel], linestyle=LINE_STYLES[fuel], linewidth=1.8, label=fuel)
    ax.set_xlabel("")
    ax.set_ylabel("RM per litre")
    ax.set_ylim(bottom=0)
    ax.legend(loc="upper left", frameon=True)
    return fig


def plot_change_frequency(frequency: pd.DataFrame) -> plt.Figure:
    """Comparison (owner: <name>): % of announcements in each year with a price change, by fuel."""
    data = frequency.reset_index().melt(id_vars="year", var_name="fuel", value_name="percent")
    data = data[data["fuel"].isin(config.MAIN_FUELS)]
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=data, x="year", y="percent", hue="fuel", hue_order=config.MAIN_FUELS,
                palette=COLOURS, ax=ax)
    for bars, hatch in zip(ax.containers, HATCHES):  # patterns, so the fuels differ without colour
        for bar in bars:
            bar.set_hatch(hatch)
            bar.set_edgecolor("white")
    ax.set_xlabel("")
    ax.set_ylabel("% of announcements with a change")
    ax.set_ylim(0, 100)
    ax.legend(title=None, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncols=3, frameon=False)
    return fig


def plot_change_distribution(changes: pd.DataFrame, fuel: str) -> plt.Figure:
    """Distribution (owner: <name>): sizes of one fuel's price changes, leaving out weeks with no change."""
    moved = changes.loc[(changes["fuel"] == fuel) & (changes["direction"] != "no change"), "change_sen"]
    bins = np.arange(moved.min() - 0.5, moved.max() + 1.5)  # one bar per whole sen
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(moved, bins=bins, color=COLOURS[fuel], edgecolor="white")
    ax.axvline(0, color="black", linewidth=1)  # rises to the right, falls to the left
    ax.set_xlabel(f"Change in the {fuel} price at one announcement (sen per litre)")
    ax.set_ylabel("Number of announcements")
    return fig
