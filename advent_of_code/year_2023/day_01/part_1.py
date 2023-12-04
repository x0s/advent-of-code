from advent_of_code.config import get_input
from advent_of_code.logging import log


class SolutionOne:
   
    @classmethod
    def process(cls, input_raw: str) -> int:
        """Find the maximum calories carried by one elf"""
        return sum(int(l[0] + l[-1]) for l in (''.join([c for c in line if c.isdigit()]) for line in input_raw.splitlines()))


def main() -> int:
    with get_input(year=2023, day=1) as input_raw:
       
        digit_sum = SolutionOne.process(input_raw)

        log.info(f"Sum found = {digit_sum}")

        # we return what's been asked
        return digit_sum

if __name__ == "__main__":
    main()
