import chess
import copy
import random
import sys
from evaluation_function import EvaluationFunction

class SmartAgent2:
    def __init__(self, color, max_depth=0):
        self.color = color
        self.max_depth = max_depth
        self.name = "SmartAgent2.5"
    
    def get_name(self):
        return self.name

    #TODO: Make this look multiple depths recursively
    def find_next_move(self, board):
        #clone the board so we don't modify something on accident
        eval = EvaluationFunction()
        current_evaluation = eval.evaluate_board(board)
        print("Current eval before selecting a move: ", eval.evaluate_board(board))
        print(board.legal_moves)
        
        number_of_legal_moves = len(list(board.legal_moves))
        if number_of_legal_moves > 1:
            random_move_index = random.randint(0, number_of_legal_moves-1)
            random_move = list(board.legal_moves)[random_move_index]
            
            best_evaluation = current_evaluation #sys.maxsize if self.color == chess.BLACK else -sys.maxsize-1
            best_move = random_move
            for move in board.legal_moves:
                board_copy = copy.deepcopy(board)
                board_copy.push(move)
                val, _ = self.minimax_chess(board_copy, self.max_depth, self.color)
                if self.color == chess.WHITE and val > best_evaluation:
                    best_evaluation = val
                    best_move = move
                    print("Found best move for white! ", best_evaluation, board.san(best_move))
                elif self.color == chess.BLACK and val < best_evaluation:
                    best_evaluation = val
                    best_move = move
                    print("Found best move for black! ", best_evaluation, board.san(best_move))
            print("Making eval & move: ", best_evaluation, board.san(best_move))
            return best_move
        
        else:
            return list(board.legal_moves)[0] #return the only move available

    def minimax_chess(self, current_board, depth, maximizing_color):
        eval = EvaluationFunction()
        current_eval = eval.evaluate_board(current_board)
        if depth == 0: #Leaf Node --> Here's where we evaluate! 
            return current_eval, current_board.peek() #return this eval and move that was committed. 
        #returning this move doesn't make sense.. because a leaf node move ultimatley won't be the right move.. it will be a parent move.
        
        # print("depth: ", depth)
        # print("color: ", maximizing_color)

        copied_board = copy.deepcopy(current_board)
        value = current_eval
        best_move = None
        if (maximizing_color == chess.WHITE):

            for move in copied_board.legal_moves:
                # print("Evaluating move: ", move)
                next_move_board = copy.deepcopy(current_board)#implement this legal move
                next_move_board.push(move)
                evaluated_value, evaluated_move = self.minimax_chess(next_move_board, depth-1, chess.BLACK)
                if evaluated_value > value:
                    # print("Found a better move for white!!! ", copied_board.san(evaluated_move))
                    # print("eval value: ", evaluated_value)
                    value = evaluated_value
                    best_move = move
            # print("eval value: ", value)
            return value, best_move 
        
        else:

            for move in copied_board.legal_moves:
                next_move_board = copy.deepcopy(current_board)#implement this legal move
                next_move_board.push(move)
                evaluated_value, evaluated_move = self.minimax_chess(next_move_board, depth-1, chess.WHITE)
                if evaluated_value <= value:
                    # print("Found a better move for white!!! ", copied_board.san(evaluated_move))
                    # print("eval value: ", evaluated_value)                    
                    value = evaluated_value
                    best_move = move
            return value, best_move
    
#MINIMAX PSEUDOCODE!
#function minimax(node, depth, maximizingPlayer) is
#     if depth = 0 or node is a terminal node then
#         return the heuristic value of node
#     if maximizingPlayer then
#         value := −∞
#         for each child of node do
#             value := max(value, minimax(child, depth − 1, FALSE))
#         return value
#     else (* minimizing player *)
#         value := +∞
#         for each child of node do
#             value := min(value, minimax(child, depth − 1, TRUE))
#         return value
# (* Initial call *)
# minimax(origin, depth, TRUE)