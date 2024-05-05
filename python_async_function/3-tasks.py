#!/usr/bin/env python3
"""
Tasks
"""
import asyncio

task_wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that returns an asyncio.Task
    """
    return asyncio.create_task(task_wait_random(max_delay))
