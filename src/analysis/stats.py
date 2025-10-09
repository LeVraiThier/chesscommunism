import pandas as pd

def compute_stats(df: pd.DataFrame):
    stats = {}

    winrate = (df["result"] == "win").mean() * 100
    stats["Winrate global"] = f"{winrate:.2f}%"

    color_stats = (df.groupby("color")["result"].value_counts(normalize=True).unstack(fill_value=0) * 100).round(2)
    stats["Winrate par couleur"] = color_stats

    category_counts = df["category"].value_counts()
    stats["Répartition par cadence"] = category_counts

    openings = df["opening_name"].value_counts().head(5)
    stats["Top 5 ouvertures"] = openings

    return stats