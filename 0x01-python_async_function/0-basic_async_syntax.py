#!/usr/bin/env python3
"""Module to demonstrate basic asynchronous syntax with random delays."""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay.

    Args:
        max_delay (int): The maximum number of seconds to wait. Defaults to 10.

    Returns:
        float: The actual delay time waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
