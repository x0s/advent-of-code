
from itertools import cycle, zip_longest
from typing import Iterable


from advent_of_code.config import get_input
from advent_of_code.logging import log


# (rock_id, move_id) -> (rock_num, height)
RecordType = dict[tuple[int], tuple[int]]
# Store blocked positions in tower
TowerType = set[tuple]
# A rock is represented by the coordinates of its pixels
RockType = set[tuple]

class SolutionOne:

    rocks_raw = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""

    directions = {'>': (+1,  0), # right
                  '<': (-1,  0), # left
                  '|': ( 0, -1)} # down

    @staticmethod
    def tuple_add(a: tuple, b: tuple) -> tuple:
        return (a[0] + b[0]), (a[1] + b[1])

    @classmethod
    def get_direction(cls, input_raw: str) -> Iterable[tuple[int, tuple]]:
        jets = [jet for jet in input_raw.rstrip()]
        # insert "down":| move every 'left':> or 'right':< moves
        moves = cycle(enumerate([move for move_with_down in zip_longest(jets, [], fillvalue='|')
                                      for move in move_with_down if move]))
        for index, move in moves:
            yield index,cls.directions[move]

    @staticmethod
    def is_blocked(rock: RockType, tower: TowerType) -> bool:
        return (bool(tower & rock) or 
                not all((0 <= x < 7 and y >= 0) for (x,y) in rock))

    @staticmethod
    def get_height(tower: TowerType) -> int:
        return  (max(tower, key=lambda x_y: x_y[1])[1] + 1) if len(tower) > 0 else 0

    @classmethod
    def process(cls, input_raw: str, n_rocks: int) -> int:
        
        rocks = [{(i, j) for j,line in enumerate(rock.splitlines()[::-1]) 
                 for i,c in enumerate(line) if c =='#'} 
                 for rock in cls.rocks_raw.split('\n\n')]

        gap_down = 3
        gap_left = 2
        offset_start = (gap_left, gap_down)
        tower : TowerType = set()
        records: RecordType = {}
        iter_direction = cls.get_direction(input_raw)

        for rock_num,(rock_id, rock) in enumerate(cycle(enumerate(rocks))):
            if rock_num >= n_rocks: break

            offset = (gap_left, 3+1+max(tower, key=lambda x_y: x_y[1])[1]) if rock_num>0 else offset_start
            rock = {cls.tuple_add(pixel, offset) for pixel in rock}

            while True:
                move_id, direction = next(iter_direction)
                rock_prev = rock
                # Let's see where <would> be the next position if we really make this move
                rock = {cls.tuple_add(pixel, direction) for pixel in rock}

                # Have we already seen this rock moving this way ?
                if (key := (rock_id, move_id)) in records:
                    rock_num_prev, height = records[key]
                    rock_num_delta = rock_num - rock_num_prev
                    # Can we see this pattern repeating until all rocks would have fallen ?
                    if rock_num % rock_num_delta == n_rocks % rock_num_delta:
                        log.info(f"Cycle consisting of {rock_num_delta} rocks")
                        height_delta = cls.get_height(tower) - height
                        n_rocks_left = n_rocks - rock_num
                        cycles_left = (n_rocks_left // rock_num_delta) + 1
                        return height + height_delta * cycles_left
                else:
                    records[key] = (rock_num, cls.get_height(tower))

                if cls.is_blocked(rock, tower):
                    if direction[1] == -1:       # if going down
                        tower.update(rock_prev)
                        break
                    elif abs(direction[0]) == 1: # if going laterally
                        rock = rock_prev
                        continue

        return cls.get_height(tower)


def main() -> int:
    with get_input(year=2022, day=17) as input_raw:
       
        total = SolutionOne.process(input_raw, n_rocks=2022)

        log.info(f"How many units tall will the tower of rocks be after 2022 rocks have stopped falling? {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
