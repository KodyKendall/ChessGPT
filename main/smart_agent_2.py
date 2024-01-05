import chess
import copy
import random
from evaluation_function import EvaluationFunction

class SmartAgent2:
    def __init__(self, color, max_depth=0):
        self.color = color
        self.max_depth = max_depth
    
    #TODO: Make this look multiple depths recursively
    def find_next_move(self, board):
        #clone the board so we don't modify something on accident
        eval = EvaluationFunction()
        print(board.legal_moves)
        
        number_of_legal_moves = len(list(board.legal_moves))
        if number_of_legal_moves > 1:
            random_move_index = random.randint(0, number_of_legal_moves-1)
            random_move = list(board.legal_moves)[random_move_index]
            
            best_evaluation = 0
            best_move_so_far = random_move
            best_move, best_eval = self.evaluate_next_move(board, 0, best_move_so_far, best_evaluation, self.color)
            return best_move
        
        else:
            return list(board.legal_moves)[0] #return the only move available

    def evaluate_next_move(self, board, depth, best_move_so_far, best_evaluation, current_color):
        print("Evaluating move for color: ", current_color)        
        
        #base case:
        if depth > self.max_depth:
            return best_move_so_far, best_evaluation
        
        board_copy = copy.deepcopy(board)

        best_move_from_here = best_move_so_far
        best_evaluation_from_here = best_evaluation

        #get all legal_moves and evaluate them using evaluate_next_move
        for index, _ in enumerate(board_copy.legal_moves):
                #find the best move from the legal_moves
                move_to_evaluate = list(board_copy.legal_moves)[index]
                board_copy.push(move_to_evaluate)
                
                color_to_evaluate_for = chess.WHITE if current_color == chess.BLACK else chess.BLACK
                best_move, eval_score = self.evaluate_next_move(board_copy, depth+1, best_move_so_far, best_evaluation, color_to_evaluate_for)
                # eval_score = eval.evaluate_board(board_copy)
            
                if self.color == chess.WHITE and eval_score > best_evaluation:
                    best_evaluation_from_here = eval_score
                    best_move_from_here = best_move
                elif self.color == chess.BLACK and eval_score < best_evaluation:
                    best_evaluation_from_here = eval_score
                    best_move_from_here = best_move

                board_copy.pop()

        return best_move_from_here, best_evaluation_from_here