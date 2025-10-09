from src.api.chesscom_client import ChesscomClient
from src.analysis.clean import clean_games
from src.analysis.stats import compute_stats


client = ChesscomClient("Hikaru")
games = client.get_all_games(limit=500)
df = client.games_to_dataframe(games,)
df_clean = clean_games(df, "Hikaru")

stats = compute_stats(df_clean)

for k, v in stats.items():
    print(f"\n--> {k}:")
    print(v)