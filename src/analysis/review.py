import io
import chess.pgn
import chess.engine

class Review:
    def __init__(self, engine_path="stockfish"):
        self.engine_path = engine_path

    def load_game_from_pgn(self, pgn_text):
        pgn_io = io.StringIO(pgn_text)
        game = chess.pgn.read_game(pgn_io)
        return game

    def evaluate_game(self, game, depth=15):
        engine = chess.engine.SimpleEngine.popen_uci(self.engine_path)
        

        engine.configure({
            "Threads": 4,   
            "Hash": 512     
        })

        board = game.board()
        evals = []

        for move in game.mainline_moves():
            board.push(move)
            info = engine.analyse(
                board,
                chess.engine.Limit(depth=depth),
                multipv=2
            )
            
            score = info[0]["score"].pov(board.turn).score(mate_score=10000)
            evals.append(score)

        engine.quit()
        return evals

    def detect_mistakes(self, evals):
        diffs = [evals[i] - evals[i-1] for i in range(1, len(evals))]
        annotations = []
        for d in diffs:
            if d < -300:
                annotations.append("blunder")
            elif d < -150:
                annotations.append("mistake")
            elif d < -60:
                annotations.append("inaccuracy")
            else:
                annotations.append("good")
        return ["good"] + annotations

    def review_game(self, pgn_text, depth=15):
        game = self.load_game_from_pgn(pgn_text)
        evals = self.evaluate_game(game, depth)
        labels = self.detect_mistakes(evals)

        board = game.board()
        for i, (move, score, label) in enumerate(zip(game.mainline_moves(), evals, labels)):
            san = board.san(move)
            print(f"{i+1}. {san:8} ({score:+}) -> {label}")
            board.push(move)
