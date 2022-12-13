from io import StringIO
from itertools import permutations
import numpy as np
import networkx as nx

from advent_of_code.config import get_input
from advent_of_code.logging import log


class SolutionOne:

    def __init__(self, input_raw: str):
        self.mountain = np.genfromtxt(StringIO(input_raw), delimiter=1, dtype=str)

        self.coords_S = self.get_coords('S', self.mountain)[0]
        self.coords_E = self.get_coords('E', self.mountain)[0]
        self.mountain[self.coords_S] = 'a'
        self.mountain[self.coords_E] = 'z'


    @staticmethod
    def get_coords(letter: str, array: np.ndarray) -> list[tuple]:
        return [tuple(coord) for coord in np.argwhere(array == letter)]

    @staticmethod
    def infer_graph(mountain: np.ndarray) -> nx.DiGraph:
        G = nx.DiGraph()
        """
        (i,j)---(i,j+1)
            |
        (i+1,j)
        """
        height, width = mountain.shape
        for i,j in np.ndindex(mountain.shape):
            nodes = [(i,j)] + (j+1<width)*[(i,j+1)] + (i+1<height)*[(i+1,j)]
            pairs = [combi for combi in permutations(nodes, r=2) if (i,j) in combi]

            for pred,succ in pairs:
                if ord(mountain[succ]) - ord(mountain[pred]) <= 1: # If climbable +0 or +1 elevation
                    G.add_edge(pred, succ)
        return G

    def process(self) -> int:
        G = self.infer_graph(self.mountain)

        return len(nx.dijkstra_path(G, self.coords_S, self.coords_E))-1


def main() -> int:
    with get_input(year=2022, day=12) as input_raw:
       
        total = SolutionOne(input_raw).process()

        log.info(f"What is the fewest steps required to move from your current position to the location that should get the best signal? = {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
