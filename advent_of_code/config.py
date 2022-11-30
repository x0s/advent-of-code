import requests
import tomllib
from typing import Iterator

from contextlib import contextmanager
from pathlib import Path



def get_token(config_file: str="config.toml") -> str:
    """Get token from TOML config file"""
    # Read config to get connexion settings (ie: token)
    with open(Path(__file__).resolve().parent / config_file, "rb") as f:
        CONFIG = tomllib.load(f)
    return CONFIG['token']


@contextmanager
def get_input(year: int, day: int) -> Iterator[str]:
    """Get input data from remote aoc server for a given year/day"""
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    with requests.get(url, cookies={"session": get_token()}) as input_raw:
        yield input_raw.text