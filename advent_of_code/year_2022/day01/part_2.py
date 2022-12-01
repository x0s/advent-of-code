from advent_of_code.config import get_input
from advent_of_code.logging import log
from .part_1 import sum_perf_elf

   
def part_two(input_raw: str) -> int:
    """Find total Calories carried by the three Elves carrying the most"""
    return sum(sorted(sum_perf_elf(input_raw))[-3:])


def main() -> int:
    with get_input(year=2022, day=1) as input_raw:
       
        total_calories = part_two(input_raw)

        log.info(f"Total calories carried by the 3 Elves carrying the most = {total_calories}")

        # we return what's been asked
        return total_calories

if __name__ == "__main__":
    main()
