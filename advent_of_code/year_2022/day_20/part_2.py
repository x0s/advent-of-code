from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_20.part_1 import SolutionOne, FileDecryptor


class SolutionTwo(SolutionOne):

    @classmethod
    def process(cls, input_raw: str) -> int:
            return (FileDecryptor(input_raw,
                                  decryption_key=811589153).mix(n=10)
                                                           .grove_coordinates())


def main() -> int:
    with get_input(year=2022, day=20) as input_raw:

        total = SolutionTwo.process(input_raw)

        log.info(f"hat is the sum of the three numbers that form the grove coordinates? {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
