#!/usr/bin/env python3
"""
An iterable object
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function to return a list of tuples containing elements and their lengths.
    """
    return [(i, len(i)) for i in lst]
