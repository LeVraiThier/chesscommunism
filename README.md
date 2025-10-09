#  Chesscommunism

**Chesscommunism** is a personal chess data analysis project focused on chess.com games.  
It fetches your games via the chess.com API, cleans and structures the data, computes statistics,  
and provides detailed move-by-move analysis using the Stockfish engine.

---

##  Features

-  Fetches all games from the chess.com public API  
-  Cleans and standardizes game data (colors, results, time controls, openings)  
-  Computes player statistics:
-  Move-by-move game review using Stockfish 

---

## 🧱 Project Structure

- `src/api/` — Handles chess.com API communication  
- `src/analysis/` — Data cleaning, stats, and game review logic  
- `stockfish/` — Local folder for the Stockfish engine (not included in Git)
- `main.py` — Simple driver script to test the full pipeline  

---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/LeVraiThier/chesscommunism.git
cd chesscommunism
```

### 2. Install dependencies
```bash
pip install -r requirements.txt 
```

### 3. Add the Stockfish engine
See [stockfish/README.md](./stockfish/README.md) for details.

## Usage
```bash
python main.py
```

For now, it fetches all games from your chess.com account and ptints summary statistics
#### Example
##### Inputs:
- username = hikaru
- limit = 500
```bash
--> Winrate global:
82.80%

--> Winrate par couleur:
result  draw   loss    win
color
black   6.17  11.93  81.89
white   8.95   7.39  83.66

--> Répartition par cadence:
category
blitz     368
bullet    132
Name: count, dtype: int64

--> Top 5 ouvertures:
opening_name
Nimzowitsch Larsen Attack Classical Variation 2.Bb2 Bf5          7
Nimzowitsch Larsen Attack Modern Variation 2.Bb2 Nc6 3.c4 Nf6    7
Trompowsky Attack 2...d5 3.e3                                    5
Nimzowitsch Larsen Attack Classical Variation 2.Bb2 Nf6          5
Modern Defense Standard Line 3...c6 4.Be3 d5 5.e5                5
Name: count, dtype: int64
```
