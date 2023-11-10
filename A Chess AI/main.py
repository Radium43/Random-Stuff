import chess
import chess.svg

def UseBrainShit(board):
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 100
    }

    return sum([piece_values[piece.piece_type] for piece in board.piece_map().values()])

def MoveShit(board):
    legal_moves = list(board.legal_moves)
    best_move = legal_moves[0]
    best_eval = float('-inf')

    for move in legal_moves:
        board.push(move)
        eval = -UseBrainShit(board)
        if eval > best_eval:
            best_eval = eval
            best_move = move
        board.pop()

    return best_move

def play_chess():
    board = chess.Board()

    while not board.is_game_over():
        print(board)
        
        if board.turn == chess.WHITE:
            move = MoveShit(board)
            board.push(move)
            print(f"AI plays: {move.uci()}")
        else:
            user_move = input("your move (UCI format, e.g, 'e2e4'): ")
            board.push(chess.Move.from_uci(user_move))

    print("Game Over")
    print("Result: " + board.result())

if __name__ == "__main__":
    play_chess()

'''
Thanks to one of my friends for some help on this
'''