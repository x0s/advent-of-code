from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_03.part_1 import SolutionOne


class SolutionTwo:
    
    @staticmethod
    def process(input_raw: str) -> int:
        """Compute the priority sums"""
        sacks = input_raw.strip().split('\n')
        return sum([SolutionOne.priority((set(sacks[i]) & set(sacks[i+1]) & set(sacks[i+2])).pop()) for i,_ in enumerate(sacks) if i%3==0 ])


def main() -> int:
    with get_input(year=2022, day=3) as input_raw:
       
        priority_sum = SolutionTwo.process(input_raw)

        log.info(f"Priority sum = {priority_sum}")

        # we return what's been asked
        return priority_sum

if __name__ == "__main__":
    main()
