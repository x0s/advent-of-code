from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_06.part_1 import SolutionOne


class SolutionTwo(SolutionOne):
    
    @classmethod
    def process(cls, input_raw: str) -> int:
        """How many characters need to be processed before
        the first start-of-message marker is detected?"""
        return cls.get_marker_index(input_raw, 14)


def main() -> int:
    with get_input(year=2022, day=6) as input_raw:
       
        index = SolutionTwo.process(input_raw)

        log.info(f"start-of-message at index = {index}")

        # we return what's been asked
        return index

if __name__ == "__main__":
    main()
