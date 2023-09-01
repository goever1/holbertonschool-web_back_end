#!/usr/bin/env python3
"""Async Generation"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def mesure_time(n: int, max_delay: int) -> float:
    """It returns total_time / n"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total =  end - start
    return total / n
