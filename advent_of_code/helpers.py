import logging

from collections.abc import Iterable, Iterator
from contextlib import contextmanager
from operator import add
from typing import TypeVar

YieldValue = TypeVar('YieldValue')
AnyTupleNumber = tuple[int | float, ...]

def takewhile_inc(max_value: float, iterable: Iterable[YieldValue]) -> Iterator[YieldValue]:
    # takewhile inclusive (x<5, [1,4,9,2]) --> 1 4 9
    for x in iterable:
        if x < max_value:
            yield x
        else:
            yield x
            break

@contextmanager
def logging_level(level: str | int) -> Iterator[None]:
    if not isinstance(level, int):
        level = level.upper()
    logging.disable(level)
    try:
        yield
    finally:
        logging.disable('CRITICAL')

def tuple_add(a: AnyTupleNumber, b: AnyTupleNumber) -> AnyTupleNumber:
    return tuple(map(add, a, b))