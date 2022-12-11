import heapq
import re
from collections import deque
from dataclasses import dataclass
from functools import partial
from itertools import chain, tee
from operator import add, mul
from typing import Callable, Self

from advent_of_code.config import get_input
from advent_of_code.logging import log


OperatorType = Callable[[int, int], int]

@dataclass
class Item:
    level: int

class Extractor:
    @staticmethod
    def get_int(string: str) -> int:
        return [int(i) for i in re.findall(r'\b\d+\b', string)][0]
    
    @staticmethod
    def get_items(string: str) -> deque[Item]:
        return deque([Item(int(item_level)) for item_level in re.findall(r'\b\d+\b', string)])
    
    @staticmethod
    def get_operation(string: str):
        square = lambda level: level*level
        match string.lstrip().split('Operation: new = old ')[1:][0].split(' '):
            case ['*', val]: op = partial(mul, int(val)) if val.isdigit() else square  
            case ['+', val]: op = partial(add, int(val))
        return op
    
    @classmethod
    def get_buddies(cls, raw_buddy_1: str, raw_buddy_2: str) -> tuple[int]:
        return (cls.get_int(raw_buddy_1), cls.get_int(raw_buddy_2))


@dataclass
class Monkey:
    id: int
    divisor: int
    operation: OperatorType
    buddies: tuple[id]
    items: deque[Item]
    inspections: int = 0
        
    def inspect(self, with_booster=None) -> None:
        item = self.items.popleft()
        item.level = (self.operation(item.level) % with_booster if with_booster else 
                      self.operation(item.level) // 3)
        self.inspections += 1
        return self.test(item.level), item
    
    def test(self, item_level: int) -> None:
        return self.buddies[0] if item_level % self.divisor == 0 else self.buddies[1]
    
    @staticmethod
    def make(raw_id, raw_items, raw_operation, raw_divisor, *raw_buddies) -> Self:
        e = Extractor()
        return Monkey(id        = e.get_int(raw_id),
                      items     = e.get_items(raw_items),
                      operation = e.get_operation(raw_operation),
                      divisor   = e.get_int(raw_divisor),
                      buddies   = e.get_buddies(*raw_buddies))


def monkey_business(monkeys: dict[int, Monkey]) -> int:
    return mul(*heapq.nlargest(2, (monkey.inspections for monkey in monkeys)))



class SolutionOne:

    @classmethod
    def process(cls, input_raw: str) -> int:
        monkeys = [Monkey.make(*monkey_raw.splitlines()) for monkey_raw in input_raw.split('\n\n')]
    
        n_rounds = 20
        for monkey in chain.from_iterable(tee(monkeys, n_rounds)):
            for _ in range(len(monkey.items)):
                monkey_receiver, item = monkey.inspect()
                monkeys[monkey_receiver].items.append(item)

        return monkey_business(monkeys)


def main() -> int:
    with get_input(year=2022, day=11) as input_raw:
       
        total = SolutionOne.process(input_raw)

        log.info(f"What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans? = {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
