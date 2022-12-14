from dataclasses import dataclass
from itertools import pairwise
from operator import add, sub
from typing import Self

from advent_of_code.config import get_input
from advent_of_code.logging import log


class PointSet(set):
    @property
    def max_y(self):
        return max(self, key=lambda point: point.y).y
        

@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int
    
    def __add__(self, point: Self): return Point(*map(add, (self.x, self.y), (point.x, point.y)))
    def __sub__(self, point: Self): return Point(*map(sub, (self.x, self.y), (point.x, point.y)))
    
    @classmethod
    def from_str(cls, string: str) -> Self:
        return cls(*map(int, string.split(',')))
    
    @classmethod
    def sample(self, from_: Self, to_: Self) -> PointSet:
        """Sample points between from_ and to_ (including them). works only on straight lines"""
        to_, from_ = (from_, to_) if (from_.x > to_.x or from_.y > to_.y) else (to_, from_)
        return PointSet({from_ + Point(0, i) for i in range(to_.y - from_.y + 1)}.union(
                        {from_ + Point(i, 0) for i in range(to_.x - from_.x + 1)}))


class Cave:

    def __init__(self, input_raw: str, floor_offset: int | float = float('inf')) -> None:
        paths = [path.split(' -> ') for path in input_raw.splitlines()]
        paths = [list(map(Point.from_str, lines)) for lines in paths]
        
        self.blocked = PointSet()
        for lines in paths:
            for a, b in pairwise(lines):
                self.blocked.update(Point.sample(a, b))
        
        self.rock_len = len(self.blocked)
        self.loop_max_y = self.blocked.max_y

        if floor_offset != float('inf'):
             self.loop_max_y += floor_offset 
        self.floor_y = self.blocked.max_y + floor_offset

    
    def is_blocked(self, sand: Point) -> bool:
        return (sand in self.blocked) or (sand.y >= self.floor_y)

    def next_coord(self, sand: Point) -> Point | None:
        if   not self.is_blocked((new := sand + Point( 0, 1))): return new
        elif not self.is_blocked((new := sand + Point(-1, 1))): return new
        elif not self.is_blocked((new := sand + Point(+1, 1))): return new
        else: self.blocked.update({sand})
    
    def pour(self):
        sand = Point(500, 0)
        while sand is not None and sand.y < self.loop_max_y:
            # trying to pour, if blocked, try to start with new sand
            if (sand := self.next_coord(sand)) is None:
                if(sand := Point(500,0)) in self.blocked: break
    @property
    def n_resting(self):
        return len(self.blocked) - self.rock_len

class SolutionOne:
    @classmethod
    def process(self, input_raw) -> int:
        cave = Cave(input_raw)
        cave.pour()
        return cave.n_resting


def main() -> int:
    with get_input(year=2022, day=14) as input_raw:
       
        total = SolutionOne.process(input_raw)

        log.info(f"How many units of sand come to rest before sand starts flowing into the abyss below?= {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
