from typing import Iterator

from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_21.part_1 import SolutionOne, NumberNotFound


class SolutionTwo(SolutionOne):

    op_inv = {'+': '-',
              '-': '+',
              '*': '/',
              '/': '*'}
        
    @classmethod
    def inverse_operation(cls, monkey_moving: str, operation: str, from_the_right: bool) -> tuple[str, str]:
        """Solve 1rd order equation by making the monkey variable (either a or b) become monkey moving
        Example:
            "gamma", "X + beta"     (X on the left so from_the_right is False) becomes
            "X"    , "gamma - beta" (we moved gamma on the left, returning False)
        """
        match operation.split():
            # moving = a + b --> (b = moving - a) OR (a = moving - b)
            case [monkey_a, '+', monkey_b]:
                if from_the_right: return monkey_b, f"{monkey_moving} - {monkey_a}"
                else:              return monkey_a, f"{monkey_moving} - {monkey_b}"
            
            # moving = a - b --> (a = moving + b) OR (b = a - moving)
            # moving = a / b --> (a = moving * b) OR (b = a / moving)
            case [monkey_a, ('-' | '/') as op , monkey_b]:
                if from_the_right: return monkey_b, f"{monkey_a} {op} {monkey_moving}"
                else:              return monkey_a, f"{monkey_b} {cls.op_inv[op]} {monkey_moving}"

            # moving = a * b --> (a = moving / b) OR (b = moving / a)
            case [monkey_a, '*' , monkey_b]:
                if from_the_right: return monkey_b, f"{monkey_moving} / {monkey_a}"
                else:              return monkey_a, f"{monkey_moving} / {monkey_b}"
        
            case _:
                raise ValueError(f"operation {operation} not inverted")

    @staticmethod
    def search_operation(X: str, monkey_number: str, exclude: set = None) -> Iterator[tuple[str, str, bool]]:
        """Search for the operation with monkey variable X as operand
        Return:
        - the monkey that should yell the result of operation (ie "pppw")
        - the operation (ie: "cczh / lfqf)
        - whether the monkey variable X is positioned as right operand or not (ie: True if X=lfqf)
        """
        exclude = exclude or set()

        for monkey,operation in monkey_number.items():
            if isinstance(operation, str) and (X in operation) and (monkey not in exclude):
                yield monkey, operation, operation.endswith(X)

    def reverse_operation(self, X: str, key_treated: set) -> None:
        """ Search for operation involving monkey variable X (ie: gamma = X + beta
        - Finds         monkey_found = 'gamma', operation = 'X + beta'    , from_the_right = False (for X)
        - inverse operation, returning 'X',     operation = 'gamma - beta', from_the_right = False (for gamma)
        - Update {X: 'gamma - beta}
        - Then call recursively search for operation for 'gamma' to invert ...
        """      
        # For each unseen operations involving X
        for X_next, operation, from_the_right in self.search_operation(X, self.monkey_number.copy(), key_treated):
            # Invert the operation (making X_next the new variable)
            _, operation_inv = self.inverse_operation(X_next, operation, from_the_right)

            # Update the register with inverted operation (and delete old one)
            self.monkey_number[X] = operation_inv
            key_treated |= {X}
            del self.monkey_number[X_next]

            # Let's now go up reversing the operations of the remaining 2 operands
            monkey_left, _, monkey_right = operation_inv.split()
            self.reverse_operation(monkey_left, key_treated)
            self.reverse_operation(monkey_right, key_treated)

    def prepare_root_operation(self) -> None:
        """Update the root equation so:
        - we search for the number of one of the 2 monkeys
            - One is computable
            - the other one depend on the number we have to guess (humn)
        - the equation will reflect equality between the 2 monkeys"""
        # Let's retrieve the two monkeys that should yell the same number
        _, (monkey_a, monkey_b) = self.read_operation(self.monkey_number['root'])
        # Make unknown the number we should yell
        del self.monkey_number['humn']
        # At least one of the two monkeys knows what it should yell
        try:
            number = self.get_number(monkey_a)
        except NumberNotFound:
            number = self.get_number(monkey_b)
            self.monkey_number[monkey_b] = number
        else:
            self.monkey_number[monkey_a] = number
        finally:
            # update root equation so operands should be equal: root = a - b (with root = 0)
            self.monkey_number['root'] = self.monkey_number['root'].replace('+', '-')

    def process(self, input_raw: str) -> int:
        self.monkey_number = {monkey:int(operation) if operation.isdigit() else operation 
                                                    for line in input_raw.splitlines()
                                                    for monkey,operation in (line.split(': '),)}

        self.prepare_root_operation()

        # reverse all equations to move back up to root (updating monkey_numbers)
        self.reverse_operation('humn', key_treated=set())
        # add root equals 0 so the 2 monkeys must yell the same number
        self.monkey_number['root'] = 0
        
        # Now the problem is nicely reframed, we look for the number we should yell :)
        return int(self.get_number('humn'))


def main() -> int:
    with get_input(year=2022, day=21) as input_raw:

        total = SolutionTwo().process(input_raw)

        log.info(f"What number should I yell ? {total}")

        return total
if __name__ == "__main__":
    main()