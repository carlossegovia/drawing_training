import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

COLORS = ["#00876c", "#4e966e", "#77a475", "#9bb281", "#bcc092", "#dacfa8", "#d7b886", "#d79e6b", "#d88258",
          "#d86350", "#d43d51"]
data = "dataset/grand_slams.csv"
df = pd.read_csv(data, usecols=["year", "name", "win_count", "gender"])


def top_winners_by_year(year):
    """
    Top ten tennis players with more throphies by year
    :param year:
    :return:
    """
    df_temp = df[(df["gender"] == "Male") & (df["year"] <= year)].sort_values(by="win_count",
                                                                          ascending=False).drop_duplicates(
        ['name']).head(10)
    df_temp = df_temp.sort_values(by="win_count")
    ax.clear()

    ax.text(0, 1.15, 'GS winners from 1968 to 2019', transform=ax.transAxes, size=24, weight=600, ha='left', va='top')
    ax.text(0, 1.06, 'Number of trophies', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    plt.xticks(np.arange(0, df_temp["win_count"].max() + 1, 1))
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(1, 0.5, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(1, 0, '@carlitossegovia', transform=ax.transAxes, color='#777777', ha='right', size=5,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
    ax.barh(df_temp["name"], df_temp["win_count"], color=COLORS)
    plt.box(False)


# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=1, metadata=dict(artist='Me'), bitrate=1800)

fig, ax = plt.subplots(figsize=(15, 8))
animator = animation.FuncAnimation(fig, top_winners_by_year, frames=range(1968, 2020))
animator.save('gsw.mp4', writer=writer)
