#!/usr/bin/env python3
"""
This module is for measuring the runtime of measuring coroutines
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    This function measures the rutime of the concurrent coroutines
    """
    start = time.time()


    aw
    end = time.time()
    total_runtime = end - start
    average_runtime = total_runtime/n
    return average_runtime
