import requests
import sys
import tomllib
from typing import Iterator

from contextlib import contextmanager
from pathlib import Path


try:
    # Read config to get connexion settings (ie: token)
    with open(Path(__file__).resolve().parent / "config.toml", "rb") as f:
        CONFIG = tomllib.load(f)
except FileNotFoundError:
    # No problem if we are running tests, elsewhere we reraise
    if 'unittest' not in sys.modules:
        raise

@contextmanager
def get_input(year: int, day: int) -> Iterator[str]:
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    with requests.get(url, cookies={"session": CONFIG['token']}) as input_raw:
        yield input_raw.text