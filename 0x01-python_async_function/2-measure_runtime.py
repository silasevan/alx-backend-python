#!/usr/bin/env python3
"""Module for concurrent coroutines that returns a list of delays in ascending order."""

import asyncio
import importlib.util
from typing import List

# Specify the path to the file '0-basic_async_syntax.py'
module_name = 'basic_async_syntax'
module_path = './0-basic_async_syntax.py'

# Load the module using importlib
spec = importlib.util.spec_from_file_location(module_name, module_path)
basic_async_syntax = importlib.util.module_from_spec(spec)
spec.loader.exec_module(basic_async_syntax)

# Now you can use wait_random from the dynamically loaded module
wait_random = basic_async_syntax.wait_random

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
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays
