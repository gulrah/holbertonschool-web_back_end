#!/usr/bin/python3

from typing import Iterable, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return list of tuples containing elements and their lengths."""
    return [(i, len(i)) for i in lst]
