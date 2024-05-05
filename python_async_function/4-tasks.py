#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    completed_delays = await asyncio.gather(*delays)
    sorted_delays = sorted(completed_delays)
    return sorted_delays
