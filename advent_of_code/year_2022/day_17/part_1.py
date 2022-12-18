
import re

from itertools import cycle, zip_longest
from typing import Iterable


from advent_of_code.config import get_input
from advent_of_code.logging import log


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

    @staticmethod
    def tuple_add(a, b):
        return (a[0] + b[0]), (a[1] + b[1])

    def get_moves(input_raw: str):
        jets = [jet for jet in input_raw.rstrip()]
        # insert "down":| move every 'left':> or 'right':< moves
        moves = cycle([move for move_with_down in zip_longest(jets, [], fillvalue='|') for move in move_with_down if move])
        for move in moves:
            yield move

    @staticmethod
    def is_blocked(rock, tower):
        return (bool(tower & set(rock)) or 
                not all((0 <= x < 7 and y >= 0) for (x,y) in rock))

    @staticmethod
    def get_height(tower):
        return  max(tower, key=lambda x_y: x_y[1])[1] + 1

    @classmethod
    def process(cls, input_raw) -> int:
        directions = {'>': (+1,  0), # right
                      '<': (-1,  0), # left
                      '|': ( 0, -1)} # down
        
        rocks = [{(i, j) for j,line in enumerate(rock.splitlines()[::-1]) 
                 for i,c in enumerate(line) if c =='#'} 
                 for rock in cls.rocks_raw.split('\n\n')]

        gap_down = 3                        # distance to the highest rock(floor if first rock)
        gap_left = 2
        n_rocks =  10000                    # number of rocks about to fall
        offset_start = (gap_left, gap_down)
        tower = set()
        moves = cls.get_moves(input_raw) # cycle

        for i,rock in enumerate(cycle(rocks)):
            if i >= n_rocks: break
            new_rock = True

            not_blocked = True
            offset = (gap_left, 3+1+max(tower, key=lambda x_y: x_y[1])[1]) if i>0 else offset_start
            rock = [cls.tuple_add(pixel, offset) for pixel in rock]

            while not_blocked:

                if (direction := directions[next(moves)])[1] == -1 and new_rock == -1:
                    direction = directions[next(moves)] # first move should be left or right
                    new_rock = False

                rock_prev = rock
                rock = [cls.tuple_add(pixel, direction) for pixel in rock]

                if direction[1] == -1 and cls.is_blocked(rock, tower): # if going down and blocked
                    not_blocked = False
                    tower.update(rock_prev)
                elif abs(direction[0]) == 1 and cls.is_blocked(rock, tower): # going laterally and blocked
                    rock = rock_prev
                    continue

        return cls.get_height(tower)


def main() -> int:
    with get_input(year=2022, day=16) as input_raw:
       
        total = SolutionOne.process(input_raw)

        log.info(f"How many units tall will the tower of rocks be after 2022 rocks have stopped falling? {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
