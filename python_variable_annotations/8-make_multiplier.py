#!/usr/bin/python3

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiplier_func(n: float) -> float:
        return n * multiplier
    return multiplier_func
