import re
from collections import deque
from typing import Iterator

from advent_of_code.config import get_input
from advent_of_code.logging import log


class SolutionOne:
    
    StacksType = dict[int,deque[str]]
    MovesType = list[Iterator[int]]

    @staticmethod
    def make_moves(stacks: StacksType, moves: MovesType, crate_9001: bool = False) -> None:
        """Update in-place the stacks according to the moves"""
        reverse = lambda stack: reversed(stack) if crate_9001 else stack
        
        for n_crates,from_,to_ in moves:
            stacks[to_].extendleft(reverse([stacks[from_].popleft() for _ in range(n_crates)]))  

    @staticmethod
    def get_stacks(stacks_raw: str) -> StacksType:
        """
                    [D]          {1: deque(['N', 'Z']),
        from    [N] [C]      to   2: deque(['D', 'C', 'M']),
                [Z] [M] [P]       3: deque(['P'])}
                 1   2   3 
        """
        *stacks_lines, stacks_i = stacks_raw.splitlines()
        n_stacks = int(stacks_i.split()[-1])
        return {k+1: deque(filter(None,stack)) 
                for k,stack in enumerate(
                    zip(*[[line[i].strip() for i in range(1,len(line),4)] for line in stacks_lines]))}

    staticmethod
    def get_moves(moves_raw: str) -> MovesType:
        """
        from  "move 1 from 2 to 1   to  [[1, 2, 1], [3, 1, 3]]
               move 3 from 1 to 3"
        """
        return [map(int,re.split('move\s|\sfrom\s|\sto\s',move)[1:]) for move in moves_raw.splitlines()]
        
    @staticmethod
    def get_top_crates(stacks: StacksType) -> str:
        """
              {1: deque(['N', 'Z']),
        from   2: deque(['D', 'C', 'M']), to 'NDP'
               3: deque(['P'])}
        """
        return ''.join(stack[0] for stack in stacks.values())

    @classmethod
    def process(cls, input_raw: str) -> int:
        """What are the craters at stacks' tops after the moves ?"""
        # Treat Stacks and Moves separately 
        stacks_raw, moves_raw = input_raw.rstrip().split('\n\n')
        stacks, moves = cls.get_stacks(stacks_raw), cls.get_moves(moves_raw)
        
        # make the moves and update the stack
        cls.make_moves(stacks, moves)
        
        # return the crates at the top
        return cls.get_top_crates(stacks)


def main() -> int:
    with get_input(year=2022, day=5) as input_raw:
       
        top_crates = SolutionOne.process(input_raw)

        log.info(f"Final crates at the stacks' tops = {top_crates}")

        # we return what's been asked
        return top_crates

if __name__ == "__main__":
    main()
