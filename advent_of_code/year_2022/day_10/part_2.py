from itertools import accumulate

from advent_of_code.config import get_input
from advent_of_code.logging import log

ProgramType = dict[int, str]

class SolutionTwo:

    @staticmethod
    def get_program(input_raw: str) -> ProgramType:
        """Get the list of raw instructions index by the cycle just after completion"""
        return {cycle:instruction for instruction,cycle in zip(
                        input_raw.splitlines(),
                        accumulate((2 if instruction.startswith('addx') else 
                                    1 for instruction in input_raw.splitlines())))}

    @classmethod
    def process(cls, input_raw: str) -> None:
        x: int = 1
        row = []
        instructions = cls.get_program(input_raw)
        
        for cycle in range(240):
            if cycle in instructions:
                match instructions[cycle].split():
                    case ['addx', v]: x += int(v)
                    case ['noop']: pass
            
            x_CRT = cycle%40
            row.append('██' if x_CRT in (x-1, x, x+1) else '..')
            
            if x_CRT == 39:
                log.info(''.join(row))
                row = []


def main() -> None:
    with get_input(year=2022, day=10) as input_raw:
        SolutionTwo().process(input_raw)

if __name__ == "__main__":
    main()
