#!/usr/bin/env python3
"""Callable function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """It  returns a function that multiplies a float by multiplier"""
    return lambda x: x * multiplier
