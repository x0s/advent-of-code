from advent_of_code.config import get_input
from advent_of_code.logging import log
from advent_of_code.year_2022.day_07.part_1 import SolutionOne


class SolutionTwo(SolutionOne):
 
    @classmethod
    def process(cls, input_raw: str) -> tuple[int, int]:
        # Infer the graph from the commands execution
        G = cls.infer_tree(input_raw)

        # Compute the size of the directories (update the graph)
        occupied = cls.compute_size(G, '/')
        space_to_free = 30_000_000 - (70_000_000 - occupied)

        return min(size for size in cls.get_dir_sizes(G) if size > space_to_free), space_to_free


def main() -> int:
    with get_input(year=2022, day=7) as input_raw:
       
        size_min, space_to_free = SolutionTwo.process(input_raw)

        log.info(f"Directory of size minimum to free required space({space_to_free:,}) = {size_min:,}")

        # we return what's been asked
        return size_min

if __name__ == "__main__":
    main()
