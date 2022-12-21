import math
import re

from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_19.part_1 import SolutionOne, Factory, Blueprint


class SolutionTwo(SolutionOne):

    @classmethod
    def process(cls, input_raw: str) -> int:
        duration = 32
        blueprints = [Blueprint(*map(int, re.findall("(\d+)", line))) for line in input_raw.splitlines()]

        return math.prod(Factory(blueprint).explore(duration).max_geodes for blueprint in blueprints[:3])


def main() -> int:
    with get_input(year=2022, day=19) as input_raw:

        total = SolutionTwo.process(input_raw)

        log.info(f"What do you get if you multiply the largest number of geodes you could open in 32 minutes using the first 3 blueprints ? {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
