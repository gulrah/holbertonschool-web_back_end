#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function to return a function that multiplies a float.
    """
    def multiplier_func(n: float) -> float:
        return n * multiplier
    return multiplier_func
