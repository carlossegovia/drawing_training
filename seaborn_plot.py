import matplotlib.animation as animation
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = "dataset/grand_slams.csv"
df = pd.read_csv(data, usecols=["year", "name", "win_count", "gender"], encoding="ISO-8859-1")


def top_winners_by_year(year):
    """
    Top ten tennis players with more trophies by year
    :param year:
    :return:
    """
    df_temp = df[(df["gender"] == "Male") & (df["year"] <= year)].sort_values(by="win_count",
                                                                              ascending=False).drop_duplicates(
        ['name']).head(10)
    ax1.clear()
    sns.set(style="darkgrid")
    ax = sns.barplot(x="win_count", y="name", data=df_temp, orient="h")
    ax.set_title("GS winners")
    ax.set_xlabel("Number of trophies")
    ax.set_ylabel("Name")
    ax.text(1, 0.5, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.set_xticks(range(0, df_temp["win_count"].max() + 1, 1))


# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=1, metadata=dict(artist='Me'), bitrate=1800)

fig, ax1 = plt.subplots(figsize=(15, 8))
animator = animation.FuncAnimation(fig, top_winners_by_year, frames=range(1968, 2020))
animator.save('gsw.mp4', writer=writer)
