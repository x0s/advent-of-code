from advent_of_code.config import get_input
from advent_of_code.logging import log


class SolutionTwo:

    # Create dict of every number as string to their actual value {"eight": 8,... '4': 4}
    n_str_to_val = {**{n_str: n_val for (n_val, n_str) in enumerate("one two three four five six seven eight nine".split(), start=1)},
                    **{str(i+1): i+1 for i in range(9)}}

    # Get the length of longest number as string
    max_length = len(max(n_str_to_val.keys(), key=len))

   
    @classmethod
    def process(cls, input_raw: str) -> int:
        """Compute the sum of concatenated edged number for each line

        It works by extracting all the numbers from a sliding window of maximum numbers' length."""
        return sum(int(str(l[0]) + str(l[-1]))
                   for line in input_raw.splitlines()
                   for l in [[cls.n_str_to_val[number] 
                              for i in range(len(line))
                              for number in cls.n_str_to_val.keys() if line[i:i+cls.max_length:].find(str(number)) == 0]])


def main() -> int:
    with get_input(year=2023, day=1) as input_raw:
       
        digit_sum = SolutionTwo.process(input_raw)

        log.info(f"Sum found = {digit_sum}")

        # we return what's been asked
        return digit_sum

if __name__ == "__main__":
    main()
