import re
from collections import deque
from enum import Enum, unique
from functools import partial

from advent_of_code.config import get_input
from advent_of_code.logging import log


MoveCollection = deque[tuple[int, str]]
PositionCollection = set[complex]
EdgeCollection = dict[tuple[complex, complex], complex]


@unique
class Direction(Enum):
    down  = ( 0 + 1j)
    up    = ( 0 - 1j)
    right = (+1 + 0j)
    left  = (-1 + 0j)


class SolutionOne:

    def __init__(self) -> None:
        self.get_min_x = partial(min, key=lambda coord: coord.real)
        self.get_max_x = partial(max, key=lambda coord: coord.real)
        self.get_min_y = partial(min, key=lambda coord: coord.imag)
        self.get_max_y = partial(max, key=lambda coord: coord.imag)
    
    def infer_game(self, input_raw: str) -> None:
        """Extract wtiles, walls and moves from input"""
        board, path = input_raw.split('\n\n')

        # coordinates of open tiles and blocking walls
        self.tiles = {((k+1) + (i+1)*1j) for i,line in enumerate(board.splitlines()) for k,c in enumerate(line) if c == '.'}
        self.walls = {((k+1) + (i+1)*1j) for i,line in enumerate(board.splitlines()) for k,c in enumerate(line) if c == '#'}

        # store the path as a stack of moves
        self.moves : MoveCollection = deque([(int(m.group('tiles')), m.group('rotation'))
                                            for m in re.finditer("(?P<tiles>\d+)(?P<rotation>[LR])?", path)])

    def get_line(self, i: int) -> PositionCollection:
        return filter(lambda coord: coord.imag == i, self.tiles | self.walls)

    def get_col(self, i: int) -> PositionCollection:
        return filter(lambda coord: coord.real == i, self.tiles | self.walls)

    def infer_edges(self) -> None:
        """Extract edges all around the map in the form:
            (Edge position, direction): Position on the other side
        """
        MAX_COLS, MAX_LINES = int(self.get_max_x(self.tiles | self.walls).real), int(self.get_max_y(self.tiles | self.walls).imag)
        self.edges : EdgeCollection = {}

        for y in range(MAX_LINES):
            min_x, max_x = self.get_min_x(self.get_line(y+1)), self.get_max_x(self.get_line(y+1))
            self.edges |= {(min_x-1, Direction.left.value):  max_x,
                           (max_x+1, Direction.right.value): min_x}

        for x in range(MAX_COLS):
            min_y, max_y = self.get_min_y(self.get_col(x+1)), self.get_max_y(self.get_col(x+1))
            self.edges |= {(min_y-1j, Direction.up.value):   max_y,
                           (max_y+1j, Direction.down.value): min_y}

    def move_forward(self, from_: tuple, direction: complex, n_tiles: int) -> tuple:
        """Make n_tiles moves from a given position in some direction"""
        # According to what's next, next position will become last walked position 
        next_position = last_position = from_
        
        for i in range(n_tiles):
            # Let's see what's in next position
            next_position = next_position + direction

            # Tiles are walkable, walls are not
            if next_position in self.tiles:
                last_position = next_position
            elif next_position in self.walls:
                next_position = last_position
                break
            else:
                # Can we jump on the other side, what's there ?
                if (next_position, direction) in self.edges:
                    next_position = self.edges[(next_position, direction)]
                    if next_position in self.walls:
                        # There is wall on the other side, let's remain at previous position
                        break
                else:
                    raise ValueError(f"Out of board ! {next_position}")
        return last_position

    @staticmethod
    def compute_password(position: complex, direction: complex) -> int:
        facing = {Direction.right.value: 0,
                  Direction.down.value : 1,
                  Direction.left.value : 2,
                  Direction.up.value   : 3}[direction]
        return int(1000*position.imag + 4*position.real + facing)

    def process(self, input_raw: str) -> int:
        # Identify tiles, walls and edges in Board game
        self.infer_game(input_raw)
        self.infer_edges()

        # start in top-left corner in right direction
        last_position = self.get_min_x(self.get_line(1))
        direction = Direction.right.value

        for i,(n_tiles, rotation) in enumerate(self.moves):
            last_position = self.move_forward(last_position, direction, n_tiles)
            
            match rotation:
                case 'R': direction *= +1j
                case 'L': direction *= -1j
                case None: pass
                case _: raise ValueError(f"rotation {rotation} unknown")
        
        return self.compute_password(last_position, direction)
            

def main() -> int:
    with get_input(year=2022, day=22) as input_raw:

        total = SolutionOne().process(input_raw)

        log.info(f"hat is the final password?{total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()