#!/usr/bin/env python3
"""
This is a module for task_wait_random
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This is the concurrent coroutine function
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    for i in range(0, len(delays)):
        for j in range(i+1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]

    return delays
