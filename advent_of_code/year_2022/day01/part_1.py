from advent_of_code.config import get_input
from advent_of_code.logging import log


class SolutionOne:
    @classmethod
    def sum_per_elf(cls, input_raw: str) -> list[int]:
        """Compute the sum of calories carried by each elf"""
        return [sum(map(int, elf_cal.split('\n'))) for elf_cal in input_raw.strip().split("\n\n")]
        
    @classmethod
    def process(cls, input_raw: str) -> int:
        """Find the maximum calories carried by one elf"""
        return max(cls.sum_per_elf(input_raw))


def main() -> int:
    with get_input(year=2022, day=1) as input_raw:
       
        max_calories = SolutionOne.process(input_raw)

        log.info(f"Maximum calories carried = {max_calories}")

        # we return what's been asked
        return max_calories

if __name__ == "__main__":
    main()
