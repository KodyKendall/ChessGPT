import chess
import collections
import chess.pgn

class Helpers:
    @staticmethod
    def board_to_game(board, white_engine, black_engine):
        game = chess.pgn.Game()

        # Undo all moves.
        switchyard = collections.deque()
        while board.move_stack:
            switchyard.append(board.pop())

        game.setup(board)
        node = game

        # Replay all moves.
        while switchyard:
            move = switchyard.pop()
            node = node.add_variation(move)
            board.push(move)

        game.headers["Result"] = board.result()
        game.headers["White"] = white_engine.name
        game.headers["Black"] = black_engine.name
        return game