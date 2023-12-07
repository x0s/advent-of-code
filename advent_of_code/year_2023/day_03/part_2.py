from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2023.day_03.part_1 import SolutionOne




class SolutionTwo(SolutionOne):

    @classmethod
    def process(cls, input_raw: str) -> int:
        _, gear_set = cls.process_heaps(input_raw)
        return sum(gear for gear in gear_set)


def main() -> int:
    with get_input(year=2023, day=3) as input_raw:
       
        digit_sum = SolutionTwo.process(input_raw)

        log.info(f"Sum found = {digit_sum}")

        # we return what's been asked
        return digit_sum

if __name__ == "__main__":
    main()
