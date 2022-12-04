from advent_of_code.config import get_input
from advent_of_code.logging import log


class SolutionOne:
    
    @staticmethod
    def get_sets(pair: str) -> list[set]:
        """Generate sets given the ranges: '2-4,1-2' -> [{2, 3, 4}, {1, 2}]'"""
        range_ = lambda a,b: range(a, b+1) 
        return [set(range_(*map(int, assignement.split('-')))) for assignement in pair.split(',')]

    @classmethod
    def is_subset(cls, pair : str) -> bool:
        """'2-4,6-8' -> False / '2-4,1-6' -> True"""
        sets = cls.get_sets(pair)
        return (sets[0] <= sets[1]) or (sets[0] >= sets[1])

    @classmethod
    def process(cls, input_raw: str) -> int:
        """How many elf pairs have fully overlapping asignements ?"""
        return sum(cls.is_subset(pair) for pair in input_raw.strip().splitlines())


def main() -> int:
    with get_input(year=2022, day=4) as input_raw:
       
        n_overlapping = SolutionOne.process(input_raw)

        log.info(f"Fully overlapping assignements = {n_overlapping}")

        # we return what's been asked
        return n_overlapping

if __name__ == "__main__":
    main()
