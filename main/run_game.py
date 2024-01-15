import chess
import chess.pgn
from random_agent import RandomAgent
from smart_agent import SmartAgent
from smart_agent_2 import SmartAgent2

from helpers import Helpers

if __name__ == "__main__":
    board = chess.Board()
    # white_agent = RandomAgent(chess.WHITE)
    # black_agent = RandomAgent(chess.BLACK)
    
    white_agent = SmartAgent(chess.WHITE)
    black_agent = SmartAgent2(chess.BLACK, max_depth=2)

    while (not board.is_checkmate() and not board.is_stalemate() and not board.is_insufficient_material() and not board.is_fivefold_repetition()):
        
        if (board.turn == chess.WHITE):
            next_move = white_agent.find_next_move(board)
            board.push(next_move)
        else:
            next_move = black_agent.find_next_move(board)
            board.push(next_move)
        
        print(board)
        # input() #<-- uncomment to watch this game in real time (press enter in terminal to go to the next move)
    
    #winner is!
    print (board.outcome().termination)
    print("White!" if board.outcome().winner else ("Black!" if board.outcome().winner == False else "Draw!"))

    #Uncomment to get the PGN to evaluate with a different Chess Tool.
    print(Helpers.board_to_game(board, white_agent, black_agent))