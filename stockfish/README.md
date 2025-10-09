To use game analysis features, you must **manually download the Stockfish engine** for your system and place it here.

## Setup

1. Go to the official Stockfish website:  
    [https://stockfishchess.org/download/](https://stockfishchess.org/download/)

2. Extract or copy the Stockfish executable into this folder:

3. The project structure should look like this:
- `chesscommunism/`
  - `src/`
  - `stockfish/`
    - `stockfish executable`
    - `README.md`
  - `main.py`

4. Make sure your analysis module (`review.py`) points to the correct path, for example:
```python
ENGINE_PATH = r"chesscommunism/stockfish/stockfish.exe"