import chess

class EvaluationFunction:
    pawn_point = 1
    minor_piece_point = 3
    rook_point = 5
    queen_point = 9
    white_wins_by_checkmate = 10000
    black_wins_by_checkmate = -10000

    ### takes in a board object, and returns the evaluation. Positive number is in white's favor, negative number is in black's favor
    def evaluate_board(self, board):
        if board.is_checkmate():
            return self.white_wins_by_checkmate if board.outcome().winner == True else self.black_wins_by_checkmate

        evaluation_point = 0

        #count up all the pieces on the board from each side
        evaluation_point += (len(board.pieces(chess.PAWN, chess.WHITE)) * self.pawn_point)
        evaluation_point += (len(board.pieces(chess.BISHOP, chess.WHITE)) * self.minor_piece_point)
        evaluation_point += (len(board.pieces(chess.KNIGHT, chess.WHITE)) * self.minor_piece_point)
        evaluation_point += (len(board.pieces(chess.ROOK, chess.WHITE)) * self.rook_point)
        evaluation_point += (len(board.pieces(chess.QUEEN, chess.WHITE)) * self.queen_point)

        evaluation_point -= (len(board.pieces(chess.PAWN, chess.BLACK)) * self.pawn_point)
        evaluation_point -= (len(board.pieces(chess.BISHOP, chess.BLACK)) * self.minor_piece_point)
        evaluation_point -= (len(board.pieces(chess.KNIGHT, chess.BLACK)) * self.minor_piece_point)
        evaluation_point -= (len(board.pieces(chess.ROOK, chess.BLACK)) * self.rook_point)
        evaluation_point -= (len(board.pieces(chess.QUEEN, chess.BLACK)) * self.queen_point)

        #if you check the king, add 10.
        if board.is_check():
            # see which side is in check, deduct points from them.
            if board.turn == chess.WHITE: #white is in check, minus 10 points
                evaluation_point -= 10
            else: #black is in check, add +10 so white knows it's a good position
                evaluation_point += 10 

        return evaluation_point