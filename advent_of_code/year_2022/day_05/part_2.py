import re
from collections import deque

from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_05.part_1 import SolutionOne


class SolutionTwo(SolutionOne):
    
    @classmethod
    def process(cls, input_raw: str) -> int:
        """How many elf pairs have fully overlapping asignements ?"""
        # Treat Stacks and Moves separately 
        stacks_raw, moves_raw = input_raw.rstrip().split('\n\n')
        stacks, moves = cls.get_stacks(stacks_raw), cls.get_moves(moves_raw)
        
        # make the moves and update the stack
        cls.make_moves(stacks, moves,crate_9001=True)
        
        # return the crates at the top
        return cls.get_top_crates(stacks)


def main() -> int:
    with get_input(year=2022, day=5) as input_raw:
       
        top_crates = SolutionTwo.process(input_raw)

        log.info(f"Final crates at the stacks' tops = {top_crates}")

        # we return what's been asked
        return top_crates

if __name__ == "__main__":
    main()
