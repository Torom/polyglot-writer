import chess
from chess.polyglot import zobrist_hash

from polyglot_writer import Polyglot_Move, Polyglot_Position, Polyglot_Writer

polyglot_positions = [
    Polyglot_Position(zobrist_hash(board := chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')),
                      Polyglot_Move.from_chess_move(board, chess.Move.from_uci('e2e4')),
                      65_535,
                      0),
    Polyglot_Position(zobrist_hash(board := chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')),
                      Polyglot_Move.from_chess_move(board, chess.Move.from_uci('d2d4')),
                      65_535,
                      0),
    Polyglot_Position(zobrist_hash(board := chess.Board('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1')),
                      Polyglot_Move.from_chess_move(board, chess.Move.from_uci('e7e5')),
                      65_535,
                      0),
    Polyglot_Position(zobrist_hash(board := chess.Board('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1')),
                      Polyglot_Move.from_chess_move(board, chess.Move.from_uci('c7c5')),
                      65_535,
                      0)
]

Polyglot_Writer.write(polyglot_positions, 'example.bin')
