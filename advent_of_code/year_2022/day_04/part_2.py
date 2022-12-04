from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_04.part_1 import SolutionOne


class SolutionTwo:
    
    @staticmethod
    def does_overlap(pair : str) -> bool:
        """2-4,6-8 -> False"""
        sets = SolutionOne.get_sets(pair)
        return not sets[0].isdisjoint(sets[1])
    
    @classmethod
    def process(cls, input_raw: str) -> int:
        """How many elf pairs have partially overlapping asignements ?"""
        return sum(cls.does_overlap(pair) for pair in input_raw.strip().splitlines())


def main() -> int:
    with get_input(year=2022, day=4) as input_raw:
       
        n_overlapping = SolutionTwo.process(input_raw)

        log.info(f"Partially overlapping assignements = {n_overlapping}")

        # we return what's been asked
        return n_overlapping

if __name__ == "__main__":
    main()
