"""Shared look & feel for all figures in this repo.

Import it at the top of a notebook:

    from src.style import apply_style, COLORS, save_figure, add_footer

Nothing in here changes the numbers - it only makes the charts look consistent.
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"
FONT_DIR = ROOT / "assets" / "fonts"

# --- Colours -----------------------------------------------------------------
# Categorical colours were checked for colour-blind separation. Text never uses
# the series colours; it uses the ink colours below.
COLORS = {
    "surface": "#fcfcfb",
    "ink": "#0b0b0b",
    "ink_2": "#52514e",   # secondary text
    "ink_3": "#8a8983",   # muted text, axis lines
    "grid": "#e6e5e0",
    "no_data": "#e9e8e4",
    # fate of plastic waste
    "recycled": "#1baf7a",
    "incinerated": "#eda100",
    "landfilled": "#4a3aa7",
    "mismanaged": "#e34948",
    "open_burned": "#3d3c38",
    "ocean": "#2a78d6",
    # sources of plastic pollution (Cottom et al. 2024)
    "uncollected": "#2a78d6",
    "litter": "#eb6834",
    "disposal": "#1baf7a",
    "collection": "#eda100",
    "rejects": "#e87ba4",
}

# Single-hue sequential ramp (light -> dark) used for the choropleth maps.
MAP_RAMP = ["#fde4d6", "#f9b99a", "#f08a5e", "#d95926", "#a63d12", "#6b2408"]


def _register_fonts():
    """Use Lato if the font files are in assets/fonts, otherwise fall back quietly."""
    if not FONT_DIR.exists():
        return "DejaVu Sans"
    for ttf in FONT_DIR.glob("*.ttf"):
        font_manager.fontManager.addfont(str(ttf))
    return "Lato"


def apply_style():
    family = _register_fonts()
    mpl.rcParams.update({
        "font.family": family,
        "font.size": 11,
        "text.color": COLORS["ink"],
        "axes.labelcolor": COLORS["ink_2"],
        "axes.edgecolor": COLORS["ink_3"],
        "axes.facecolor": COLORS["surface"],
        "figure.facecolor": COLORS["surface"],
        "savefig.facecolor": COLORS["surface"],
        "xtick.color": COLORS["ink_2"],
        "ytick.color": COLORS["ink_2"],
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": False,
        "grid.color": COLORS["grid"],
        "grid.linewidth": 0.8,
        "legend.frameon": False,
        "svg.fonttype": "none",
    })


def add_title(fig, title, subtitle=None, x=0.04, top_in=0.22):
    """Title + subtitle, positioned in inches from the top so they look the same on any figure height."""
    h = fig.get_figheight()
    fig.text(x, 1 - top_in / h, title, fontsize=20, fontweight="black", va="top", ha="left")
    if subtitle:
        fig.text(x, 1 - (top_in + 0.42) / h, subtitle, fontsize=12.5, color=COLORS["ink_2"],
                 va="top", ha="left", linespacing=1.35)


def add_footer(fig, source, note=None, x=0.04, bottom_in=0.16):
    """Source line(s) + author credit at the bottom, positioned in inches from the bottom."""
    text = f"Source: {source}"
    if note:
        text += f"\n{note}"
    text += "\nChart: Maurits Kruisheer"
    fig.text(x, bottom_in / fig.get_figheight(), text, fontsize=8.8, color=COLORS["ink_3"],
             va="bottom", ha="left", linespacing=1.4)


def save_figure(fig, name, dpi=200):
    """Save as PNG (for Substack / email) and SVG (editable) in figures/."""
    FIG_DIR.mkdir(exist_ok=True)
    png = FIG_DIR / f"{name}.png"
    fig.savefig(png, dpi=dpi)
    fig.savefig(FIG_DIR / f"{name}.svg")
    print(f"saved {png.relative_to(ROOT)} (+ .svg)")
    return png
