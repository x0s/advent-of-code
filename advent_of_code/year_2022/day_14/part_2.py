from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_14.part_1 import SolutionOne,Cave


class SolutionTwo(SolutionOne):
    @classmethod
    def process(self, input_raw) -> int:
        cave = Cave(input_raw, floor_offset=2)
        cave.pour()
        return cave.n_resting

def main() -> int:
    with get_input(year=2022, day=14) as input_raw:
       
        total = SolutionTwo.process(input_raw)

        log.info(f"How many units of sand come to rest?= {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
