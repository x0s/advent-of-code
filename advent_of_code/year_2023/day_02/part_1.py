import re

from dataclasses import dataclass, fields
from functools import total_ordering
from typing import Self

from advent_of_code.config import get_input
from advent_of_code.logging import log


@dataclass
@total_ordering
class CubeSet:
    red: int = 0
    green: int = 0
    blue: int = 0

    @classmethod
    def from_string(cls, set_str: str) -> Self:
        pattern = re.compile(r"(\b\d+\b).(red|green|blue)")
        return cls(**{color: int(cubes) for (cubes,color) in [match.group(1, 2) for match in pattern.finditer(set_str)]})

    def __lt__(self, other) -> bool:
        return all(getattr(self, color.name) <= getattr(other, color.name) for color in fields(self))
    
    def get_power(self) -> int:
        return self.red * self.green * self.blue


class Game:
    bag : CubeSet = CubeSet(red=12, green=13, blue=14)

    def __init__(self, id_: int, cubes : list[CubeSet]):
        self.id = id_
        self.cubes = cubes

    def is_valid(self) -> bool:
        return all(cube <= self.bag for cube in self.cubes)
    
    @property
    def bag_min(self) -> CubeSet:
        """Get minimum bag required to play this game (used in part 2)"""
        return CubeSet(*[max(getattr(cube, color) for cube in self.cubes) for color in ('red', 'green', 'blue')])


class SolutionOne:

    @classmethod
    def get_games(cls, input_raw: str) -> list[Game]:
        # Extract Collection of game id and collection of raw strings representing each set (ie: ' 1 red, 2 green, 6 blue')
        games_raw = [(id_,game.split(';')) for (id_,game) in enumerate(input_raw.splitlines())]

        # Extract Collection of games from string reprensations of game sets
        return [Game(id_ + 1, [CubeSet.from_string(s) for s in set_strings]) for id_,set_strings in games_raw]

    @classmethod
    def process(cls, input_raw: str) -> int:
        games = cls.get_games(input_raw)
        
        return sum(game.id for game in games if game.is_valid())



def main() -> int:
    with get_input(year=2023, day=2) as input_raw:
       
        digit_sum = SolutionOne.process(input_raw)

        log.info(f"Sum found = {digit_sum}")

        # we return what's been asked
        return digit_sum

if __name__ == "__main__":
    main()
