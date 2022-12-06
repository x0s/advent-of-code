from advent_of_code.config import get_input
from advent_of_code.logging import log


class SolutionOne:
    
    @staticmethod
    def get_marker_index(buffer: str, n_distinct: int) -> int:
        for i in range(len(buffer)-n_distinct):
            if len(set(buffer[i:i+n_distinct])) == n_distinct:
                return n_distinct+i

    @classmethod
    def process(cls, input_raw: str) -> int:
        """How many characters need to be processed before 
        the first start-of-packet marker is detected?"""
        return cls.get_marker_index(input_raw, 4)


def main() -> int:
    with get_input(year=2022, day=6) as input_raw:
       
        index = SolutionOne.process(input_raw)

        log.info(f"start-of-packet at index = {index}")

        # we return what's been asked
        return index

if __name__ == "__main__":
    main()
