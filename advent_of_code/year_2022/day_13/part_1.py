import json

from advent_of_code.config import get_input
from advent_of_code.logging import log


class SolutionOne:

    @classmethod
    def compare(cls, left, right):
        """set order (for sorting between nested lists)
        ([1, 1, 3, 1, 1],  [1, 1, 5, 1, 1])   --> OK(-1)
        ([[1], [2, 3, 4]], [[1], 4])          --> OK(-1)
        ([9],              [[8, 7, 6]])       --> NO(+1)
        ([[4, 4], 4, 4],   [[4, 4], 4, 4, 4]) --> OK(-1)
        ([7, 7, 7, 7],     [7, 7, 7])         --> NO(+1)
        ([],               [3]                --> OK(-1)
        ([[[]]],           [[]]               --> NO(+1)
        ([1,[2,[3,[4,[5,6,7]]]],8,9],         --> NO(+1)
         [1,[2,[3,[4,[5,6,0]]]],8,9]
        """
        if isinstance(left, int) and isinstance(right, int):
            if left < right: return -1
            if left > right: return +1
            return 0
        else:
            left = list([left]) if isinstance(left, int) else left
            right = list([right]) if isinstance(right, int) else right
            
            if len(left) == 0 and len(right) != 0: return -1 
            if len(right) == 0 and len(left) != 0: return +1
            if len(left) == 0 and len(right) == 0: return 0
            
            if (ret := cls.compare(left[0], right[0])) != 0:
                return ret
            else:
                return cls.compare(left[1:], right[1:])

    @classmethod
    def process(cls, input_raw: str) -> int:
        pairs = [map(json.loads, pair.split()) for pair in input_raw.rstrip().split('\n\n')]
        return sum(i+1 for i,(left,right) in enumerate(pairs) if cls.compare(left, right) < 0)


def main() -> int:
    with get_input(year=2022, day=13) as input_raw:
       
        total = SolutionOne.process(input_raw)

        log.info(f"What is the sum of the indices of those pairs? = {total}")

        # we return what's been asked
        return total

if __name__ == "__main__":
    main()
