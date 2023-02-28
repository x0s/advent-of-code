from operator import add, sub, mul, truediv

from advent_of_code.config import get_input
from advent_of_code.logging import log

class NumberNotFound(KeyError):
    """Raised when a monkey number cannot be found"""

class SolutionOne:

    @staticmethod
    def read_operation(operation: str):
        match operation.split():
            case [monkey_a, '+', monkey_b]: operator = add
            case [monkey_a, '-', monkey_b]: operator = sub
            case [monkey_a, '*', monkey_b]: operator = mul
            case [monkey_a, '/', monkey_b]: operator = truediv
        return operator, (monkey_a, monkey_b)


    def get_number(self, monkey: str):
        if not monkey in self.monkey_number:
            raise NumberNotFound(f"Value for monkey={monkey} not found")
        if not isinstance((number := self.monkey_number[monkey]), (int, float)):
            do_operation, (monkey_a, monkey_b) = self.read_operation(number)
            number = do_operation(self.get_number(monkey_a), self.get_number(monkey_b))
        return number

    
    def process(self, input_raw: str) -> int:
        self.monkey_number = {monkey:int(operation) if operation.isdigit() else operation 
                                                    for line in input_raw.splitlines()
                                                    for monkey,operation in (line.split(': '),)}
        return int(self.get_number('root'))


def main() -> int:
    with get_input(year=2022, day=21) as input_raw:

        total = SolutionOne().process(input_raw)

        log.info(f"What number will the monkey named root yell? {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()