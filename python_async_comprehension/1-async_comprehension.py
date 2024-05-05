#!/usr/bin/env python3
"""
Async Comprehensions
"""
from typing import List
from random import uniform
import asyncio

async def async_generator() -> float:
    """
    Generates 10 random floats between 0 and 10 with 1 second delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)

async def async_comprehension() -> List[float]:
    """
    Collects 10 random floats using async comprehension.
    """
    result = [number async for number in async_generator()]
    return all(isinstance(number, float) for number in result), all(0 <= number <= 10 for number in result)

# For testing purposes
async def main():
    results = await async_comprehension()
    print(results)

asyncio.run(main())
