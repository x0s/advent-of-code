import requests
import sys
import tomllib
from typing import Iterator

from contextlib import contextmanager
from pathlib import Path


# If the tests are not running, we load configuration(token)
if 'unittest' not in sys.modules:
    # Read config to get connexion settings (ie: token)
    with open(Path(__file__).resolve().parent / "config.toml", "rb") as f:
        CONFIG = tomllib.load(f)

@contextmanager
def get_input(year: int, day: int) -> Iterator[str]:
    """Get input data from remote aoc server for a given year/day"""
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    with requests.get(url, cookies={"session": CONFIG['token']}) as input_raw:
        yield input_raw.text