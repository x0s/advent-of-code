import math
from itertools import chain, tee

from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_11.part_1 import SolutionOne, Monkey, monkey_business


class SolutionTwo(SolutionOne):

    @classmethod
    def process(cls, input_raw: str) -> int:
        monkeys = [Monkey.make(*monkey_raw.splitlines()) for monkey_raw in input_raw.split('\n\n')]
    
        # works with non-prime divisors
        proddiv = math.lcm(*(monkey.divisor for monkey in monkeys))
        
        n_rounds = 10_000
        for monkey in chain.from_iterable(tee(monkeys, n_rounds)):
            for _ in range(len(monkey.items)):
                monkey_receiver, item = monkey.inspect(with_booster=proddiv)
                monkeys[monkey_receiver].items.append(item)

        return monkey_business(monkeys)


def main() -> int:
    with get_input(year=2022, day=11) as input_raw:
       
        total = SolutionTwo.process(input_raw)

        log.info(f"what is the level of monkey business after 10000 rounds? = {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
