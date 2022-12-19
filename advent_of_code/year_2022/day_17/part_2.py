from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_17.part_1 import SolutionOne


def main() -> int:
    with get_input(year=2022, day=17) as input_raw:
       
        total = SolutionOne.process(input_raw, n_rocks=1_000_000_000_000)

        log.info(f"How tall will the tower be after 1000000000000 rocks have stopped? {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
