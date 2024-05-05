#!/usr/bin/env python3
"""
Tasks
"""
import asyncio
from typing import List
from asyncio import Task

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that spawns wait_random n times
    """
    tasks: List[Task] = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
