from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day02.part_1 import SolutionOne


class SolutionTwo:
    letter_to_gain = {'A': '1', 'X': '0',
                      'B': '2', 'Y': '3',
                      'C': '3', 'Z': '6'}
    
    # permute the (part 1) gains with my moves
    my_moves = {(elf,gain): me for (elf,me),gain in SolutionOne.gains.items()}

    @classmethod
    def process(self, input_raw: str) -> int:
        """Compute the total gain guessing the outcome of each game(gain)"""
        return SolutionOne.compute_gains(input_raw, self.letter_to_gain, self.my_moves) 


def main() -> int:
    with get_input(year=2022, day=2) as input_raw:
       
        gains = SolutionTwo.process(input_raw)

        log.info(f"Total gains = {gains}")

        # we return what's been asked
        return gains

if __name__ == "__main__":
    main()
