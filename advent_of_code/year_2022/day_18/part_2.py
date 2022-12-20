from collections import deque
from operator import add

import networkx as nx

from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_18.part_1 import SolutionOne, CubeType


class SolutionTwo(SolutionOne):

    @classmethod
    def infer_trapped_air(cls, G: nx.Graph) -> nx.Graph:
        """Update Cube graph so it takes into account trapped air spaces"""
        candidates = set([neighbor for node in G.nodes
                                    for neighbor in cls.get_adjacent_cubes(node)
                                    if neighbor not in G.nodes])
        
        candidates_removed = set()
        for cube in candidates:
            # If this node is already recorded as: (block or trapped air) OR (air unblocked)
            if cube not in G.nodes or cube not in candidates_removed:
                cls.search_trapped_air(cube, G, candidates_removed)
        return G

    @classmethod
    def search_trapped_air(cls, cube: CubeType, G: nx.Graph, candidates_removed: set[CubeType]) -> None:
        """Search for sequences of cubes filled with air trapped into lava and update graph
        
        Starting with <cube>, we put it in a queue of candidates (to be air trapped or not):
        - if trapped,     will be retained in <cube_air_candidates>
        - if not trapped, will be retained in <candidates_removed>
        While not too far, we look at the neighbors of the candidates,
        then we enqueue the unknown ones made of air

        We update the graph with the cubes identified as made of trapped air
        """
        cube_air_candidates = set([cube])
        queue = deque([cube])

        while queue:
            cube_pointer = queue.popleft()
            # If this candidate if already far the lava
            if len(cube_air_candidates) >= cls.INF:
                candidates_removed.update(cube_air_candidates)
                return

            for neighbor in cls.get_adjacent_cubes(cube_pointer):
                if neighbor not in cube_air_candidates and neighbor not in G.nodes:
                    cube_air_candidates.add(neighbor)
                    queue.append(neighbor)
                    
        # Update the graph with the newly discovered cube of trapped air
        for node in cube_air_candidates:
            G.add_edges_from([(node, neighbor) for neighbor in cls.get_adjacent_cubes(node)])

    @classmethod
    def process(cls, input_raw: str) -> int:
        # Extract graph of connected cubes
        G = cls.infer_graph(input_raw)
        G = cls.infer_trapped_air(G)
        return cls.compute_surface(G)


def main() -> int:
    with get_input(year=2022, day=18) as input_raw:
       
        total = SolutionTwo.process(input_raw)

        log.info(f"What is the exterior surface area of your scanned lava droplet? {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
