#!/usr/bin/env python3
"""Python async comprehension"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """It return an async comprenhension list"""
    return [i async for i in async_generator()]
