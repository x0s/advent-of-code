import networkx as nx

from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_12.part_1 import SolutionOne


class SolutionTwo(SolutionOne):

    def process(self) -> int:

        starting_points = self.get_coords('a', self.mountain)
        G = self.infer_graph(self.mountain)

        length,_ = nx.multi_source_dijkstra(G, starting_points, self.coords_E)
        return length


def main() -> int:
    with get_input(year=2022, day=12) as input_raw:
       
        total = SolutionTwo(input_raw).process()

        log.info(f"What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal? = {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
