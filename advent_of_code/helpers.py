from collections.abc import Iterable, Iterator
from typing import TypeVar

YieldValue = TypeVar('YieldValue')

def takewhile_inc(max_value: float, iterable: Iterable[YieldValue]) -> Iterator[YieldValue]:
    # takewhile inclusive (x<5, [1,4,9,2]) --> 1 4 9
    for x in iterable:
        if x < max_value:
            yield x
        else:
            yield x
            break