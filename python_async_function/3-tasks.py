#!/usr/bin/env python3
"""Async Generation"""
import asyncio
import time

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """It returns an asyncio task"""
    return asyncio.create_task(wait_random(max_delay))
