import numpy as np

from advent_of_code.config import get_input
from advent_of_code.logging import log


def larger_measurements(measurements: list[int], window_size: int=2) -> int:
    """Return how many sliding 3-windows sums are larger than their predecessor"""
    kernel = np.ones(shape=3) # Kernel <=> window of size 3 with equal weights (1, 1, 1)
    return sum(
            np.diff(
                np.convolve(measurements, kernel, 'valid') # Compute the sum over the values selected(multiplied) by the kernel(3-window)
            ) > 0)                                         # Compare the sums between current and previous result


def main() -> int:
    with get_input(year=2021, day=1) as measurements_raw:
        measurements = [int(m) for m in measurements_raw.strip().split('\n')]

        count = larger_measurements(measurements)

        log.info(f"Count of sliding 3-windows sums larger than their predecessor = {count}")

        # we return what's been asked
        return count

if __name__ == "__main__":
    main()