import math
from itertools import chain, tee

from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_11.part_1 import SolutionOne, Monkey, monkey_business


"""
Trick explanation
-----------------
Without dividing by 3 the item.level, it gets only multiplied-summed by integer or squared.
Even if it was squared only once in each round, going from 20 rounds(part 1) to 10_000 rounds(part 2)
results in generating number of immense order. Let's take a powered-by 2 item.level for convenience (ie 64): 
    
    10 rounds     : 64*64*..*64 = (2^6)^10     = 2^60     <- already close to the max size for a word
    10_000 rounds : 64^10_000   = (2^6)^10_000 = 2^10_000 <- overflow

With python, one can determine the number of bits of a signed word(int) required  to be represented with:
    math.log(sys.maxsize, 2)
    # Yields 63 (for a 64bits platform)
In Python, integers can grow unlimitedly to the memory available on the machine, but at the cost of time.
So, one won't experience typical overflow error but algorithm may take days to converge.

The trick, is to find another number that we could manipulate/store instead of the huge one.
In the algorithm, we:
- process an operation(+, *, ^2) [see: self.operation(item.level)]
- test the nullity of the remaining of the division of this evergrowing number [see: self.operation(item.level)]

pseudo-code:
    level <- operation(level)
    level % divisor == 0 ----> Monkey 2
                       /-----> Monkey 0
Example:
    [Monkey 1, divisor = 17]
    level = 55_000_000_000
    level % 17 = 11   -----> Monkey 0
    level % 17x13x19x23 = 74_539
    74_539 % 17 = 11  -----> Monkey 0
    It seems that we could manipulate 74_539 in place of 55_000_000_000

    [Monkey 0, divisor = 19]
    level <-- level*level <---operation=square
    level = 74_539^2 = 5_556_062_521
    level % 19 = 4  -----> Monkey 3
    level % 17x13x19x23 = 84_288 (always < 96577=17x13x19x23)
    84_288 % 19 = 4 -----> Monkey 3

    [Monkey 3, divisor = 23]
    level <-- level + 9 <---operation=addition
    with level = 84_288        + 9 % 23 = 16 + 9 % 23
    with level = 5_556_062_521 + 9 % 23 = 16 + 9 % 23
    Addition also does not change modular arithmetics
    level(84_297) % 23 = 4  -----> Monkey 1
    level(84_297) % 17x13x19x23 = 84_297 (already small, int nothing gained on addition) 
    level(84_297) % 23 = 4  -----> Monkey 1

    The divisor 17x13x19x23 should be the Least Common Multiple of the divisors of all monkeys
    math.lcm(monkey_divisors). In case of prime numbers, the lcm is their product, but not in general case.
    Using this trick enables us to manipulate values at maximum lcm:
    in the example lcm=96577 (requiring 17 bits to encode, way less than the 63 available for one word)

    Note that this tricks is stable by addition and multiplication but not division.

    For more info, browse https://en.wikipedia.org/wiki/Modular_arithmetic
"""


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
