from io import StringIO
from itertools import product

import numpy as np

from advent_of_code.config import get_input
from advent_of_code.logging import log


class SolutionOne:
    
    @staticmethod
    def is_visible(x: int, y: int, forest: np.ndarray) -> bool:
        """Is the tree at (x,y) is visible from outside the grid ?"""
        # Neighbors on TOP, DOWN, LEFT, RIGHT
        neighbors_groups = forest[:x, y], forest[x+1:, y], forest[x, :y], forest[x, y+1:]
        return any((forest[x,y] > neighbors).all() for neighbors in neighbors_groups)

    @staticmethod
    def get_forest(input_raw: str) -> np.ndarray:
        return np.genfromtxt(StringIO(input_raw), delimiter=1, dtype=int)
    
    @staticmethod
    def iter_trees(shape_x, shape_y):
        """Yield (x,y) of trees NOT at the edges"""
        yield from product(range(1, shape_x-1), range(1, shape_y-1))

    @classmethod
    def process(cls, input_raw: str) -> int:
        # Digitalize the trees
        forest = cls.get_forest(input_raw)
        
        # Let's already count the trees at the edge
        n_visible : int = 2*(forest.shape[0] + forest.shape[1] - 2)
        
        # how many trees are visible from outside the grid?
        n_visible += sum(cls.is_visible(tree_x, tree_y, forest) for tree_x,tree_y in cls.iter_trees(*forest.shape))
        
        return n_visible


def main() -> int:
    with get_input(year=2022, day=8) as input_raw:
       
        total = SolutionOne.process(input_raw)

        log.info(f"How many trees visible from outside the grid? = {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
