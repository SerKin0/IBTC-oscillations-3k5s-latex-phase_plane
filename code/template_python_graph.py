import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator


def apply_rcparams(size: tuple[float, float]):
    plt.rcParams.update(
        {
            "font.family": "CMU Serif",
            "font.size": 12,
            "mathtext.fontset": "cm",
            "axes.linewidth": 0.8,
            "axes.grid": True,
            "grid.linewidth": 0.4,
            "grid.alpha": 0.5,
            "xtick.direction": "in",
            "ytick.direction": "in",
            "xtick.minor.visible": True,
            "ytick.minor.visible": True,
            "xtick.major.width": 0.8,
            "ytick.major.width": 0.8,
            "xtick.minor.width": 0.4,
            "ytick.minor.width": 0.4,
            "figure.figsize": size,
            "figure.dpi": 150,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
        }
    )


def set_settings(ax):
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.grid(which="major", linewidth=0.5, alpha=0.65)
    ax.grid(which="minor", linewidth=0.25, alpha=0.4)
    ax.tick_params(which="both", top=True, right=True)
    return ax


x = [...]
y = [...]


def draw_graph(file_name: str = "graph", size: tuple = (8, 10)):
    apply_rcparams(size)
    fig, ax = plt.subplots()
    set_settings(ax)

    ax.plot(x, y, marker="o", markersize=2, linewidth=1, color="black", zorder=1)
    ax.set_xlabel(r"...")
    ax.set_ylabel(r"...")

    plt.savefig(f"{file_name}.pdf", format="pdf")
    plt.show()


if __name__ == "__main__":
    draw_graph(file_name="...", size=(12, 5))