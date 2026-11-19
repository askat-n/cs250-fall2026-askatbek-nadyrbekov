"""
charts.py  -  draw charts with matplotlib

Every chart is shown in a window AND saved as a picture in the my_charts folder.
"""


from pathlib import Path
import matplotlib.pyplot as plt
CHART_FOLDER = Path(__file__).parent / "my_charts"
RACE_CHART = CHART_FOLDER / "race_chart.png"
SEASON_CHART = CHART_FOLDER / "season_chart.png"


# -------------------------------------------------------------------
# STEP 4: a LINE chart of one race
# -------------------------------------------------------------------
def plot_race(race, filename=RACE_CHART):
    """Line chart: how far each racer had run after every round."""
    CHART_FOLDER.mkdir(exist_ok=True)
    plt.figure(figsize=(9, 5))

    for racer in race.racers:
        plt.plot(racer.history, marker="o", label=racer.name)

    # The dashed finish line (already done)
    plt.axhline(race.finish_line, color="gray", linestyle="--", label="Finish line")

    plt.title(f"Critter Grand Prix - {race.winner.name} wins!")
    plt.xlabel("Round")
    plt.ylabel("Distance")
    plt.legend()

    # Save the chart as a picture, then show it in a window (already done)
    plt.savefig(filename)
    plt.show()


# -------------------------------------------------------------------
# Already done for you: a BAR chart of a whole season (use it as a model!)
# -------------------------------------------------------------------
def plot_season(wins, filename=SEASON_CHART):
    """Bar chart: how many races each racer won in a season."""
    CHART_FOLDER.mkdir(exist_ok=True)
    plt.figure(figsize=(8, 5))

    names = list(wins.keys())
    counts = list(wins.values())
    plt.bar(names, counts, color="#4C9A8B")

    plt.title(f"Season results ({sum(counts)} races)")
    plt.xlabel("Racer")
    plt.ylabel("Number of wins")

    plt.savefig(filename)
    plt.show()
