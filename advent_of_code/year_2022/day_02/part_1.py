import re

from advent_of_code.config import get_input
from advent_of_code.logging import log


class SolutionOne:
    letter_to_val = {'A': '1', 'X': '1',
                     'B': '2', 'Y': '2',
                     'C': '3', 'Z': '3'}
    
    gains = {(3,1):6, (2,3):6, (1,2):6, # Win situations weight=6
             (1,3):0, (3,2):0, (2,1):0, # Loose  situations weight=0
             (1,1):3, (2,2):3, (3,3):3} # Draws weight=3

    @staticmethod
    def replace(string: str, replacements: dict[str, str]) -> str:
        """Replace letters by their values in a single pass
        Inspired from https://gist.github.com/bgusach/a967e0587d6e01e889fd1d776c5f3729"""
        # Create a big OR regex that matches any of the substrings to replace
        pattern = re.compile("|".join(replacements))
        
        # For each match, look up the new string in the replacements, being the key the old string
        return pattern.sub(lambda match: replacements[match.group(0)], string)

    @classmethod
    def compute_gains(cls, input_raw: str, letter_encoding: dict[str, str], gains: dict[tuple[int, int], int]) -> int:
        """Compute gains"""
        games = [map(int, battle.split(" ")) for battle in cls.replace(input_raw.strip(), letter_encoding).split('\n')]
        return sum([(bonus+gains[(elf,bonus)]) for elf,bonus in games])
        
    @classmethod
    def process(cls, input_raw: str) -> int:
        """Compute the total gain guessing the outcome of each game(gain)"""
        return cls.compute_gains(input_raw, cls.letter_to_val, cls.gains) 


def main() -> int:
    with get_input(year=2022, day=2) as input_raw:
       
        gains = SolutionOne.process(input_raw)

        log.info(f"Total gains = {gains}")

        # we return what's been asked
        return gains

if __name__ == "__main__":
    main()
