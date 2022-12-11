from advent_of_code.config import get_input
from advent_of_code.logging import log


class SolutionOne:

    @classmethod
    def process(cls, input_raw: str) -> int:
        n_cycles = 0
        x = 1
        strength = 0
        next_strength_cycle = 20

        for instruction in input_raw.splitlines():
            if n_cycles+2 >= next_strength_cycle:
                strength += next_strength_cycle*x
                next_strength_cycle += 40

            match instruction.split():
                case ['addx', v]:
                    n_cycles +=2
                    x += int(v)
                case ['noop']: n_cycles += 1
        
        return strength


def main() -> int:
    with get_input(year=2022, day=10) as input_raw:
       
        total = SolutionOne.process(input_raw)

        log.info(f"What is the sum of these six signal strengths? = {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
