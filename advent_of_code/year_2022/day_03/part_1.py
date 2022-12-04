from advent_of_code.config import get_input
from advent_of_code.logging import log


class SolutionOne:
    
    @staticmethod
    def priority(c: str) -> int:
        return ord(c)-96 if c.islower() else ord(c)-38

    @classmethod
    def process(cls, input_raw: str) -> int:
        """Compute the priority sums"""
        return sum([cls.priority((set(sack[:len(sack)//2]) & set(sack[len(sack)//2:])).pop()) for sack in input_raw.strip().split('\n')])


def main() -> int:
    with get_input(year=2022, day=3) as input_raw:
       
        priority_sum = SolutionOne.process(input_raw)

        log.info(f"Priority sum = {priority_sum}")

        # we return what's been asked
        return priority_sum

if __name__ == "__main__":
    main()
