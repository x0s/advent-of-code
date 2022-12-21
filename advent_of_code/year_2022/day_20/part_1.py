from collections import namedtuple
from typing import Self

from advent_of_code.config import get_input
from advent_of_code.logging import log


Number = namedtuple("Number", ['id', 'value'])
    

class FileDecryptor:
    """Decrypt file to get grove coordinates"""
    def __init__(self, input_raw: str, decryption_key: int = 1):
        self.buffer = [Number(id_, int(i) * decryption_key) for id_,i in enumerate(input_raw.splitlines())]
        self.buffer_len = len(self.buffer)
    
    def mix(self, n: int = 1) -> Self:
        for _ in range(n):
            for id_to_move in range(self.buffer_len):
                for index,number in enumerate(self.buffer):
                    if number.id == id_to_move:
                        self.buffer.remove(number)
                        if number.value == -index:
                            self.buffer.append(number)
                        else:
                            self.buffer.insert((index + number.value) % (self.buffer_len - 1), number)
                        break
        return self
    
    def grove_coordinates(self) -> int:
        # Retrieve index of unique zero in buffer
        zero_index = next(i for i,number in enumerate(self.buffer) if number.value == 0)
        # sum over the 1000, 2000 and 3000th numbers after 0
        return sum(self.buffer[(zero_index + offset) % self.buffer_len].value for offset in (1000, 2000, 3000))


class SolutionOne:

    @classmethod
    def process(cls, input_raw: str) -> int:
        return (FileDecryptor(input_raw).mix()
                                        .grove_coordinates())


def main() -> int:
    with get_input(year=2022, day=20) as input_raw:

        total = SolutionOne.process(input_raw)

        log.info(f"hat is the sum of the three numbers that form the grove coordinates? {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
