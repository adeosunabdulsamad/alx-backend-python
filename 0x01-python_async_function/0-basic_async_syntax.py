#!/usr/bin/env python3
"""
This is an async function module
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Thos is the wait_random fuctio that uses asynchronous coroutine
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
