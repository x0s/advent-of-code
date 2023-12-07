import re
from dataclasses import dataclass, field

from advent_of_code.config import get_input
from advent_of_code.logging import log


@dataclass(frozen=True)
class Coord:
    i: int   # index of line
    j: int   # index of starting column
    jc: int  # index of ending column + 1 (= j + length)

@dataclass
class Item:
    value: str
    is_star: bool = False
    adjacents : list = field(default_factory=list) # if an item is adjacent to a number (only for * chars)

HeapType = dict[Coord, Item]

def drop_line(heap: HeapType, line_i: int) -> HeapType:
    """Remove from the heap elements recorded in line i.
    Returns a heap containing only the removed elements"""
    return {coord: heap.pop(coord) for coord in list(heap) if coord.i == line_i}

def save_gears(heap: HeapType) -> list[int]:
    # saving gears from heap before it can be dropped
    return [(item.adjacents[0] * item.adjacents[1]) for coord, item in heap.items() 
            if item.is_star and 
            len(item.adjacents) == 2] if heap is not None else None

class SolutionOne:

    @classmethod
    def process_heaps(cls, input_raw: str) -> tuple[HeapType, list[int]]:
        heap_to_check : HeapType = dict()  # Numbers to check (to keep or not)
        heap_to_keep  : HeapType = dict()  # Numbers to keep (that are connected to a char)
        heap_char     : HeapType = dict()  # Characters recorded
        gear_set : list[int] = list()      # Adjacents numbers to stars

        # Extract any number or character that is not a dot nor a line break
        pattern = re.compile(r"(\b\d+\b|[^.\n])")

        for i, line in enumerate(input_raw.splitlines()):
            for match in pattern.finditer(line):
                coord = Coord(*((i,) + match.span()))             # (line, column_start, column_start+length)
                if((value := match.group()).isdigit()): # Record value
                    heap_to_check[coord] = Item(value)
                else:
                    heap_char[coord] = Item(value, is_star=(value=='*'))           # Record coord of char
            # drop lines that are too far (numbers not connected and every character)
            _, heap_char_removed = drop_line(heap_to_check, i-2), drop_line(heap_char, i-2)
            # At removal, we check if gears has been tied to star(*) char, and save
            gear_set.extend(save_gears(heap_char_removed))
            
            # check if remaining values are to be kept
            # for each char, check if it is neighbour to any digit (O(n_chars_neighbours x n_numbers_to_check))
            for char,char_item in heap_char.items():
                for number in list(heap_to_check):
                    if (number.i-1 <= char.i <= number.i+1 and
                        number.j-1 <= char.j <= number.jc):
                        #print(f"We found a connected number : {heap_to_check[number]}")
                        heap_to_keep[number] = heap_to_check.pop(number)

                        if char_item.is_star:
                            # We found a star close to a number")
                            heap_char[char].adjacents.append(int(heap_to_keep[number].value))
        
        # Saving gears for the 2 last lines
        gear_set.extend(save_gears(drop_line(heap_char, i-1))) 
        gear_set.extend(save_gears(drop_line(heap_char, i))) 

        return heap_to_keep, gear_set
        
    
    @classmethod
    def process(cls, input_raw: str) -> int:
        heap_to_keep, _ = cls.process_heaps(input_raw)
        return sum(int(number.value) for number in heap_to_keep.values())
    
    @classmethod
    def process__(cls, input_raw: str) -> int:
        _, _gear_set = cls.process_heaps(input_raw)
        return sum(gear for gear in gear_set)


def main() -> int:
    with get_input(year=2023, day=3) as input_raw:
       
        digit_sum = SolutionOne.process(input_raw)

        log.info(f"Sum found = {digit_sum}")

        # we return what's been asked
        return digit_sum

if __name__ == "__main__":
    main()
