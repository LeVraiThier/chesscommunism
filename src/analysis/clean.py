import pandas as pd 
from datetime import datetime

def clean_games(df: pd.DataFrame, username: str) -> pd.DataFrame:
    username = username.lower()

    df["color"] = df.apply(lambda r:"white" if r["white"].lower() == username else "black", axis = 1)
    df["opponent"] =  df.apply(lambda r: r["black"] if r["color"] == "white" else r["white"], axis = 1)

    def get_results(row):
        res = row["result_white"] if row["color"] == "white" else row["result_black"]

        if res == "win":
            return "win"
        
        elif res in ["agreed", "stalemate", "repetition", "insufficient"]:
            return "draw"
        
        else:
            return "loss"

    def format_time_control(tc):
        if not isinstance(tc, str) or tc.strip() in ["", "-", "None", "null"]:
            return "unknown"

        tc = tc.strip()

        if "/" in tc:
            try:
                base, seconds = tc.split("/")
                days = int(seconds) // 86400
                return f"{base} move / {days} days"
            except Exception:
                return "unknown"

        if "+" in tc:
            try:
                base, inc = tc.split("+")
                mins = int(base) // 60 if base.isdigit() else 0
                return f"{mins}mins+{inc}"
            except Exception:
                return "unknown"

        if tc.isdigit():
            mins = int(tc) // 60
            return f"{mins}+0"

        return "unknown"
        
    def categorize(tc):
        if not isinstance(tc, str) or tc in ["", "-", "unknown"]:
            return "unknown"

        if "days" in tc:
            return "daily"

        try:
            base_str = tc.split("+")[0].replace("mins", "")
            base = int(base_str)
        except Exception:
            return "unknown"

        if base < 3:
            return "bullet"
        elif base < 10:
            return "blitz"
        elif base <= 60:
            return "rapid"
        else:
            return "classical"
    
        
    df["time_control"] = df["time_control"].apply(format_time_control)
    df["category"] = df["time_control"].apply(categorize)
    df["result"] = df.apply(get_results, axis = 1)
    df["date"] = pd.to_datetime(df["end_time"], unit="s")
    df["opening_name"] = df["eco"].apply(lambda x: x.split("/")[-1].replace("-"," ") if isinstance(x, str) and "chess.com/openings" in x else x)

    return df[["date", "color","result","opponent","category","time_control","opening_name","url"]]