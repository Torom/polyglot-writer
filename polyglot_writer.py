import chess


class Polyglot_Move(int):
    @classmethod
    def from_chess_move(cls, board: chess.Board, move: chess.Move) -> 'Polyglot_Move':
        if board.is_castling(move):
            if chess.square_file(move.to_square) > chess.square_file(move.from_square):  # kingside castling
                move.to_square = chess.H1 if board.turn else chess.H8
            elif chess.square_file(move.to_square) < chess.square_file(move.from_square):  # queenside castling
                move.to_square = chess.A1 if board.turn else chess.A8

        to_file = chess.square_file(move.to_square)
        to_row = chess.square_rank(move.to_square)
        from_file = chess.square_file(move.from_square)
        from_row = chess.square_rank(move.from_square)

        promotion_piece = move.promotion - 1 if move.promotion else 0

        return cls(to_file
                   | (to_row << 3)
                   | (from_file << 6)
                   | (from_row << 9)
                   | (promotion_piece << 12))


class Polyglot_Position:
    def __init__(self, zobrist_hash: int, polyglot_move: int, weight: int, learn: int) -> None:
        self.zobrist_hash = zobrist_hash
        self.polyglot_move = polyglot_move
        self.weight = weight
        self.learn = learn

    def to_bytes(self) -> list[bytes]:
        return [
            self.zobrist_hash.to_bytes(8, byteorder='big', signed=False),
            self.polyglot_move.to_bytes(2, byteorder='big', signed=False),
            self.weight.to_bytes(2, byteorder='big', signed=False),
            self.learn.to_bytes(4, byteorder='big', signed=False)
        ]


class Polyglot_Writer:
    @staticmethod
    def write(polyglot_positions: list[Polyglot_Position], file_name: str) -> None:
        polyglot_positions.sort(key=lambda entry: entry.zobrist_hash)

        with open(file_name, 'wb') as output:
            for polyglot_position in polyglot_positions:
                for byte in polyglot_position.to_bytes():
                    output.write(byte)
