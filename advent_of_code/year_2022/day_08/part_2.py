from functools import reduce
from operator import mul

import numpy as np

from advent_of_code.helpers import takewhile_inc
from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_08.part_1 import SolutionOne


class SolutionTwo(SolutionOne):

    @staticmethod
    def scenic_score(x: int, y: int, forest: np.ndarray) -> bool:
        """How far can we see from the tree(x,y) ?"""
        # Neighbors on TOP, DOWN, LEFT, RIGHT but FROM the tree 
        neighbors_groups = forest[:x, y][::-1], forest[x+1:, y], forest[x, :y][::-1], forest[x, y+1:]
        n_trees = [sum(1 for _ in takewhile_inc(forest[x,y], neighbors)) for neighbors in neighbors_groups]
        return reduce(mul, n_trees)

    @classmethod
    def process(cls, input_raw: str) -> int:
        # Digitalize the trees
        forest = cls.get_forest(input_raw)
        
        # Maximum visibility(scenic score) observed from inside the forest
        return max([cls.scenic_score(tree_x, tree_y, forest) for tree_x,tree_y in cls.iter_trees(*forest.shape)])


def main() -> int:
    with get_input(year=2022, day=8) as input_raw:
       
        total = SolutionTwo.process(input_raw)

        log.info(f"How far is it possible to see from the forest ? {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
