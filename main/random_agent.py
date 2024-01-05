# This "agent" is the bot that will play against an opponent.
# Given a current board position of chess, this agent will find the next move and execute it to move the board game forward
import chess
import random

class RandomAgent:
    def __init__(self, color):
        self.color = color
        
    def find_next_move(self, board):
        #the most basic version of this game is to just find a random next move and play it. 
        print(board.legal_moves)
        print("Randomly picking a move!")
        number_of_legal_moves = len(list(board.legal_moves))
        if number_of_legal_moves > 1:
            random_move_index = random.randint(0, number_of_legal_moves-1)
            random_move = list(board.legal_moves)[random_move_index]
            return random_move
        else:
            return list(board.legal_moves)[0] #return last move

if __name__ == "__main__":
    print("hello world")
    board = chess.Board()
    while (not board.is_checkmate() and not board.is_stalemate() and not board.is_insufficient_material()):
        next_move = find_next_move(board)
        board.push(next_move)
        print(board)
    
    #winner is!
    print(board.outcome().winner)