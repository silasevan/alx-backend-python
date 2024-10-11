#!/usr/bin/env python3
from typing import List

"""
This module defines a function that calculates the sum of a list of floats.
"""

def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floating-point numbers and returns the result.

    Args:
        input_list (List[float]): A list of floats to sum.

    Returns:
        float: The sum of the floats in the input list.
    """
    return sum(input_list)
