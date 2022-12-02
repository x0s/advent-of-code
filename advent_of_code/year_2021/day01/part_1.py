import pandas as pd

from advent_of_code.config import get_input
from advent_of_code.logging import log


def larger_measurements(measurements: list[int], window_size: int=2) -> int:
    """Return how many measurements are larger than the previous measurement"""
    return pd.Series(measurements).rolling(window_size).apply(lambda x: x.iloc[1] > x.iloc[0]).sum().astype(int)


def main() -> int:
    with get_input(year=2021, day=1) as measurements_raw:
        measurements = [int(m) for m in measurements_raw.strip().split('\n')]

        count = larger_measurements(measurements)

        log.info(f"Count of measurements larger than their predecessor = {count}")

        # we return what's been asked
        return count

if __name__ == "__main__":
    main()