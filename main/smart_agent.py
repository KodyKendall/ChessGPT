import chess
import copy
import random
from evaluation_function import EvaluationFunction

class SmartAgent:
    def __init__(self, color):
        self.color = color
        self.name = "SmartAgent1.0"

    def get_name(self):
        return self.name
    
    def find_next_move(self, board):
        #clone the board so we don't modify something on accident
        eval = EvaluationFunction()
        print(board.legal_moves)
        
        number_of_legal_moves = len(list(board.legal_moves))
        if number_of_legal_moves > 1:
            board_copy = copy.deepcopy(board)
            
            random_move_index = random.randint(0, number_of_legal_moves-1)
            random_move = list(board.legal_moves)[random_move_index]
            
            best_evaluation = 0
            best_move_so_far = random_move

            for index, _ in enumerate(board.legal_moves):
                move_to_evaluate = list(board.legal_moves)[index]
                board_copy.push(move_to_evaluate)
                eval_score = eval.evaluate_board(board_copy)
            
                if self.color == chess.WHITE and eval_score > best_evaluation:
                    best_evaluation = eval_score
                    best_move_so_far = move_to_evaluate
                elif self.color == chess.BLACK and eval_score < best_evaluation:
                    best_evaluation = eval_score
                    best_move_so_far = move_to_evaluate

                board_copy.pop()

            return best_move_so_far
        
        else:
            return list(board.legal_moves)[0] #return the only move available
