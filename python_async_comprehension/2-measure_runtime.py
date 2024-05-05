#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import asyncio
from time import perf_counter
from typing import List
from itertools import measure_runtime, async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime
    """
    start_time = perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = perf_counter()
    return end_time - start_time
