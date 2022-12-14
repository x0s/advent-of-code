from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_14.part_1 import SolutionOne


def main() -> int:
    with get_input(year=2022, day=14) as input_raw:
       
        total = SolutionOne(input_raw, floor_offset=2).process()

        log.info(f"How many units of sand come to rest?= {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
