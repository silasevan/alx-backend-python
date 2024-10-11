#!/usr/bin/env python3
import math

"""
This module defines a function that returns the floor of a floating-point number.
"""

def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number.

    Args:
        n (float): The floating-point number to floor.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
