#!/usr/bin/env python3
"""Module for concurrent coroutines that returns a list of delays in ascending order."""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return the list
    of delays in ascending order without using sort().

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of all delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    
    return sorted(delays)  # Sort the list manually by adding each as it finishes
