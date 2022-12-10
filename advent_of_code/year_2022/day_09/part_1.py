from dataclasses import dataclass

import numpy as np

from advent_of_code.config import get_input
from advent_of_code.logging import log


@dataclass
class Knot:
    x: int
    y: int
    
    def __sub__(self, knot):
        return Knot(self.x - knot.x, self.y - knot.y)
    
    def norm(self):
        return np.linalg.norm([self.x, self.y])


class SolutionOne:

    @staticmethod
    def is_adjacent(tail, head):
        """on side OR diagonal OR overlapped"""
        return (head - tail).norm() < 2

    @staticmethod
    def make_adjacent(tail, head):
        tail.x += (tail.x != head.x) * np.sign(head.x - tail.x)
        tail.y += (tail.y != head.y) * np.sign(head.y - tail.y)

    @classmethod
    def process(cls, input_raw: str) -> int:
        motions = [direction_steps.split(' ') for direction_steps in input_raw.splitlines()]

        head, tail = Knot(0, 0), Knot(0, 0)
        tail_positions = {(tail.x, tail.y)}

        for direction, steps in motions:
            for i in range(1, int(steps)+1):
                match direction:
                    case 'R': head.x += 1
                    case 'L': head.x -= 1
                    case 'U': head.y += 1
                    case 'D': head.y -= 1
                if not cls.is_adjacent(tail, head):
                    cls.make_adjacent(tail, head)
                    tail_positions.add((tail.x, tail.y))
        
        return len(tail_positions)


def main() -> int:
    with get_input(year=2022, day=9) as input_raw:
       
        total = SolutionOne.process(input_raw)

        log.info(f"How many positions does the tail of the rope visit at least once? = {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
