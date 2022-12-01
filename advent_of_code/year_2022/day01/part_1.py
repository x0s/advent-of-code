from advent_of_code.config import get_input
from advent_of_code.logging import log


def sum_per_elf(input_raw: str) -> list[int]:
    """Compute the sum of calories carried by each elf"""
    return [sum(map(int, elf_cal.split('\n'))) for elf_cal in input_raw.strip().split("\n\n")]
    
def part_one(input_raw: str) -> int:
    """Find the maximum calories carried by one elf"""
    return max(sum_per_elf(input_raw))


def main() -> int:
    with get_input(year=2022, day=1) as input_raw:
       
        max_calories = part_one(input_raw)

        log.info(f"Maximum calories carried = {max_calories}")

        # we return what's been asked
        return max_calories

if __name__ == "__main__":
    main()
