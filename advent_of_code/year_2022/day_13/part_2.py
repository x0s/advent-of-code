import json
from functools import cmp_to_key

from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_13.part_1 import SolutionOne


class SolutionTwo(SolutionOne):


    @classmethod
    def process(cls, input_raw: str) -> int:
        packets = [json.loads(p) for p in input_raw.rstrip().split('\n') if len(p)>0]
        packets.extend([[[2]], [[6]]])
        packets.sort(key=cmp_to_key(cls.compare))
        return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


def main() -> int:
    with get_input(year=2022, day=13) as input_raw:
       
        total = SolutionTwo.process(input_raw)

        log.info(f"What is the decoder key for the distress signal? = {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
