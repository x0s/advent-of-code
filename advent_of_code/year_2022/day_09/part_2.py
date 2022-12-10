from dataclasses import dataclass

import numpy as np

from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_09.part_1 import SolutionOne, Knot


class SolutionTwo(SolutionOne):

    @classmethod
    def process(cls, input_raw: str) -> int:
        motions = [direction_steps.split(' ') for direction_steps in input_raw.splitlines()]

        n_knots = 10
        rope = [Knot(0, 0) for _ in range(n_knots)]
        tail_positions = {(rope[n_knots-1].x, rope[n_knots-1].y)}

        for direction, steps in motions:
            for _ in range(1, int(steps)+1):
                match direction:
                    case 'R': rope[0].x += 1
                    case 'L': rope[0].x -= 1
                    case 'U': rope[0].y += 1
                    case 'D': rope[0].y -= 1
                for k in range(n_knots-1):
                    if not cls.is_adjacent(rope[k+1], rope[k]):
                        cls.make_adjacent(rope[k+1], rope[k])
                        if k+1 == n_knots-1:
                            tail_positions.add((rope[n_knots-1].x, rope[n_knots-1].y))
        
        return len(tail_positions)


def main() -> int:
    with get_input(year=2022, day=9) as input_raw:
       
        total = SolutionTwo.process(input_raw)

        log.info(f"How many positions does the tail of the rope visit at least once? = {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
