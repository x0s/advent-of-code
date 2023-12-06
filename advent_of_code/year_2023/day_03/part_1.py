import re
from dataclasses import dataclass

from advent_of_code.config import get_input
from advent_of_code.logging import log


@dataclass(frozen=True)
class Coord:
    i: int   # index of line
    j: int   # index of starting column
    jc: int  # index of ending column + 1 (= j + length)

@dataclass
class Item:
    #coord : Coord
    value: str
    adjacents : tuple = None # if an item is adjacent to a number (only for * chars)


def drop_lines(heap: dict[Coord, Item], threshold: int) -> int:
    """Remove from the heap elements recorded in lines < threshold.
    Returns the number of elements removed"""
    return len([heap.pop(coord) for coord in list(heap) if coord.i < threshold])


class SolutionOne:

    @classmethod
    def process(cls, input_raw: str) -> int:
        heap_to_check : dict[Coord, Item] = dict()  # Numbers to check (to keep or not)
        heap_to_keep  : dict[Coord, Item] = dict()  # Numbers to keep (that are connected to a char)
        heap_char     : dict[Coord, Item] = dict()  #

        # Extract any number or character that is not a dot nor a line break
        pattern = re.compile(r"(\b\d+\b|[^.\n])")

        i = 0
        for i, line in enumerate(input_raw.splitlines()):
            for match in pattern.finditer(line):
                coord = Coord(*((i,) + match.span()))             # (line, column_start, column_start+length)
                if((value := match.group()).isdigit()): # Record value
                    heap_to_check[coord] = Item(value)
                else:
                    heap_char[coord] = Item(value)           # Record coord of char
            # drop lines that are too far (numbers not connected and every character)
            drop_lines(heap_to_check, i-2)
            drop_lines(heap_char, i-2)
            
            # check if remaining values are to be kept
            # for each char, check if it is neighbour to any digit (O(n_chars_neighbours x n_numbers_to_check))
            for char in heap_char:
                for number in list(heap_to_check):
                    if (number.i-1 <= char.i <= number.i+1 and
                        number.j-1 <= char.j <= number.jc):
                        #print(f"We found a connected number : {heap_to_check[number]}")
                        heap_to_keep[number] = heap_to_check.pop(number)
                
        return sum(int(number.value) for number in heap_to_keep.values())
        



def main() -> int:
    with get_input(year=2023, day=3) as input_raw:
       
        digit_sum = SolutionOne.process(input_raw)

        log.info(f"Sum found = {digit_sum}")

        # we return what's been asked
        return digit_sum

if __name__ == "__main__":
    main()
