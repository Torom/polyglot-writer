# polyglot-writer
Small code snippet to create polyglot books with python-chess.

## Usage
The `Polyglot_Writer.write()` function needs a list of `Polyglot_Position` and a path under which the book should be written.

A `Polyglot_Position` consists of the zobrist hash of the position, a `Polyglot_Move`, the weight and the learn values.

A `Polyglot_Move` is a move serialized to an integer. For this the `Polyglot_Move.from_chess_move()` function can be used.

## Example
This example creates a polyglot book under the name `example.bin`. The book contains for the starting position the moves e4 and d4 with equal weighting and for the position after 1. e4 it contains e5 and c5 with equal weight.

```python
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
```

## Acknowledgements
[Polyglot book format](http://hgm.nubati.net/book_format.html) by Harm Geert Muller

## License
This code is licensed under the GPLv3 (or any later version at your option). Check out the [LICENSE file](/LICENSE) for the full text.