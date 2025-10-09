import requests
import pandas as pd
from typing import List, Dict, Any

class ChesscomClient:
    
    BASE_URL = "https://api.chess.com/pub/player"
    HEADERS = {'User-Agent': 'chesscommunism/1.0'}

    def __init__(self, username):
        self.username = username.lower().strip()
    
    def _get(self, endpoint) -> Dict[str, Any]:
        url = f"{self.BASE_URL}/{self.username}/{endpoint}"
        response = requests.get(url, headers=self.HEADERS)
        if response.status_code != 200:
            raise Exception(f"Error: HTTP {response.status_code} on {url}")
        return response.json()

    def get_archives(self) -> List[str]:
        url = f"{self.BASE_URL}/{self.username}/games/archives"
        data = requests.get(url, headers=self.HEADERS).json()
        return data.get("archives", [])
    
    def get_month_games(self, archive_url) -> List[Dict[str, Any]]:
        data = requests.get(archive_url, headers=self.HEADERS).json()
        return data.get("games",[])
    
    def get_all_games(self, limit = None) -> List[Dict[str, Any]]:
        archives = self.get_archives()
        all_games = []
        for url in archives[::-1]:
            games = self.get_month_games(url)
            all_games.extend(games)
            if limit and len(all_games) >= limit:
                break
        return all_games[:limit] if limit else all_games
    
    def games_to_dataframe(self, games) -> pd.DataFrame:
        rows = []
        for g in games:
            rows.append({
                "url": g.get("url"),
                "end_time": g.get("end_time"),
                "time_control": g.get("time_control"),
                "rules": g.get("rules"),
                "result_white": g.get("white", {}).get("result"),
                "result_black": g.get("black", {}).get("result"),
                "white": g.get("white", {}).get("username"),
                "black": g.get("black", {}).get("username"),
                "pgn": g.get("pgn", ""),
                "eco": g.get("eco"),
                "opening": g.get("opening", {}).get("name") if isinstance(g.get("opening"), dict) else g.get("opening"),
            })
        return pd.DataFrame(rows)
