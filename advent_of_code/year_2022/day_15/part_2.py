import re

NUMBA_AVAILABLE = True
try:
    from numba import njit
    from numba.core import types
    from numba.typed import Dict
except ImportError:
    NUMBA_AVAILABLE = False

from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_15.part_1 import SolutionOne, try_numba


class SolutionTwo(SolutionOne):
    
    @try_numba
    @staticmethod
    def tuple_add(a, b):
        return (a[0] + b[0]), (a[1] + b[1])

    @try_numba
    @staticmethod
    def from_iterable(iterables):
        # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
        for it in iterables:
            for element in it:
                yield element

    @try_numba
    @classmethod
    def search_beacon(cls, sensor_dist: dict[tuple, int], val_max: int=20):
        directions = {(+1, +1), (-1, +1), (-1, -1), (+1, -1)}
        beacon = (0, 0)
        
        for (xS, yS),dS in sensor_dist.items():
            # Let's evaluate at the borders
            x,y = xS, yS-(dS+1)
            for direction in cls.from_iterable([[direction]*(dS+1) for direction in directions]):
                # is this border point part of another surface ?
                if (not 0 <= x <= val_max) or (not 0 <= y <= val_max): continue
                for (xS_neighbour, yS_neighbour),dS_neighbour in sensor_dist.items():
                    if cls.d((x, y), (xS_neighbour, yS_neighbour)) <= dS_neighbour:
                        found = False
                        beacon = (0, 0)
                        break
                    else:
                        found = True
                        beacon = (x, y)
                if found: return beacon
                #if not found, we look around another surface
                x,y = cls.tuple_add((x,y), direction)
        return beacon
   
    @classmethod
    def process(cls, input_raw: str) -> int:
        if not NUMBA_AVAILABLE:
            raise NotImplementedError("Numba is required for this solution")

        coords = [list(map(int,re.findall('-?\d+\.?\d*', line))) for line in input_raw.splitlines()]
    
        sensor_dist = Dict.empty(
                key_type   = types.UniTuple(types.int64, 2), 
                value_type = types.int64)
        
        for (xS,yS,xB,yB) in coords:
            sensor_dist[(xS, yS)] = cls.d((xS, yS), (xB, yB))
        
        beacon = cls.search_beacon(sensor_dist, y_row=4_000_000)

        return 4_000_000*beacon[0] + beacon[2]


def main() -> int:
    with get_input(year=2022, day=15) as input_raw:
       
        total = SolutionTwo.process(input_raw)

        log.info(f"Find the only possible position for the distress beacon. What is its tuning frequency? {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
