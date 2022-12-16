import re

NUMBA_AVAILABLE : bool = True
try:
    from numba import njit
    from numba.core import types
    from numba.typed import Dict
except ImportError:
    NUMBA_AVAILABLE = False

from advent_of_code.config import get_input
from advent_of_code.logging import log

def try_numba(func, *args, **kws):
    if NUMBA_AVAILABLE:
        return njit(func, *args, **kws)
    else:
        return func


class SolutionOne:
    
    @try_numba
    @staticmethod
    def d(a: tuple, b: tuple) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    @try_numba
    @classmethod
    def get_n_occupied(cls, sensor_dist: dict[tuple, int], x_min: int, x_max: int, y_row: int) -> int:
        total = 0
        for x in range(x_min, x_max+1):
            found = False
            for (xS, yS),dS in sensor_dist.items():
                if cls.d((x, y_row), (xS, yS)) <= dS:
                    found = True
            if found: total +=1
        return total

    @classmethod
    def process(cls, input_raw: str, y_row: int) -> int:
        coords = [list(map(int,re.findall('-?\d+\.?\d*', line))) for line in input_raw.splitlines()]
        
        if NUMBA_AVAILABLE:
            sensor_dist = Dict.empty(
                    key_type   = types.UniTuple(types.int64, 2), 
                    value_type = types.int64)
            
            for (xS,yS,xB,yB) in coords:
                sensor_dist[(xS, yS)] = d((xS, yS), (xB, yB))
        else:
            sensor_dist = {(xS, yS): cls.d((xS, yS), (xB, yB)) for (xS, yS,xB, yB) in coords}
        
        beacons = {(xB, yB) for (_,_,xB,yB) in coords}

        x_min = min([xS-d for (xS, _),d in sensor_dist.items()])
        x_max = max([xS+d for (xS, _),d in sensor_dist.items()])
        
        
        if NUMBA_AVAILABLE:
            n_occupied = cls.get_n_occupied(sensor_dist, x_min, x_max, y_row)
        else:
            n_occupied = sum([any(cls.d((x, y_row), (xS, yS)) <= dS for (xS, yS),dS in sensor_dist.items()) for x in range(x_min, x_max+1)])
        n_beacons = sum(1 if yB==y_row else 0 for _,yB in beacons)
        return n_occupied - n_beacons


def main(y_row: int = 2_000_000) -> int:
    with get_input(year=2022, day=15) as input_raw:
       
        total = SolutionOne.process(input_raw, y_row)

        log.info(f"In the row where y=2000000, how many positions cannot contain a beacon?= {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
