import math

from itertools import permutations
from typing import Iterable

import networkx as nx

from advent_of_code.config import get_input
from advent_of_code.helpers import tuple_add
from advent_of_code.logging import log

CubeType = tuple[int, int, int]

class SolutionOne:

    directions = [tuple((-1)**(i%2)*coord for coord in coords) 
                  for i,coords in enumerate(sorted(permutations([1, 0, 0])))]

    @classmethod
    def get_adjacent_cubes(cls, cube: CubeType) -> Iterable[CubeType]:
        for direction in cls.directions:
            yield tuple_add(cube, direction)

    @classmethod
    def infer_graph(cls, input_raw: str) -> nx.Graph:
        cubes = [tuple(map(int, line.split(','))) for line in input_raw.splitlines()]
        G = nx.Graph()

        for cube in cubes:
            G.add_node(cube)
            # Let's tie this new cube to potential neigbours already registered
            for neighbor in cls.get_adjacent_cubes(cube):
                if neighbor in G.nodes:
                    G.add_edge(cube, neighbor)

        # There's no more chance of closing the air cavity if we are far from lava
        cls.INF = math.prod(max(G.nodes, key=math.prod)) # max(x*y*z) for all cubes
        return G

    @staticmethod
    def compute_surface(G: nx.Graph) -> int:
        return sum(6 - G.degree(cube) for cube in G.nodes)

    @classmethod
    def process(cls, input_raw: str) -> int:
        # Extract graph of connected cubes
        G = cls.infer_graph(input_raw)
        return cls.compute_surface(G)


def main() -> int:
    with get_input(year=2022, day=18) as input_raw:
       
        total = SolutionOne.process(input_raw)

        log.info(f"What is the surface area of your scanned lava droplet? {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
