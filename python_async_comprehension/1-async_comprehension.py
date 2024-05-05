#!/usr/bin/env python3
"""
Async Comprehensions
"""
from typing import List
from itertools import async_comprehension


async def async_comprehension() -> List[float]:
    """
    Asynchronous comprehension that collects 10 random numbers.
    """
    return [i async for i in async_generator()]
