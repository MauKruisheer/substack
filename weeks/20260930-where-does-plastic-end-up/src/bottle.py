"""A tiny bottle icon for matplotlib, used in the 'where does plastic end up' figure."""
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle


def draw_bottle(ax, x, y, w, color, fill_fraction=1.0, outline=None, lw=1.0, zorder=3):
    """Draw a bottle with its bottom-left corner at (x, y) and width w (height is 2.3 * w).

    fill_fraction < 1 draws only the bottom part filled (e.g. 0.3 of a bottle),
    with the rest as an outline.
    """
    h = 2.3 * w
    body_top = 0.66 * h
    neck_w = 0.40 * w
    neck_x = x + (w - neck_w) / 2
    shoulder_top = 0.82 * h
    neck_top = 0.90 * h
    cap_w = 0.50 * w
    cap_x = x + (w - cap_w) / 2

    shape = [
        (x, y + 0.08 * h), (x + 0.04 * w, y), (x + 0.96 * w, y), (x + w, y + 0.08 * h),
        (x + w, y + body_top),
        (neck_x + neck_w, y + shoulder_top), (neck_x + neck_w, y + neck_top),
        (neck_x, y + neck_top), (neck_x, y + shoulder_top),
        (x, y + body_top),
    ]
    cap = Rectangle((cap_x, y + neck_top), cap_w, h - neck_top, linewidth=0)

    if fill_fraction >= 1:
        ax.add_patch(Polygon(shape, closed=True, facecolor=color, edgecolor="none", zorder=zorder))
        cap.set_facecolor(color)
        ax.add_patch(cap)
        return

    # partly filled: outline of the whole bottle + filled bottom part
    edge = outline or color
    ax.add_patch(Polygon(shape, closed=True, facecolor="none", edgecolor=edge, linewidth=lw,
                         linestyle=(0, (2, 1.5)), zorder=zorder))
    fill_h = fill_fraction * body_top
    ax.add_patch(FancyBboxPatch((x, y), w, fill_h, boxstyle="round,pad=0,rounding_size=0.04",
                                facecolor=color, edgecolor="none", zorder=zorder + 1))
