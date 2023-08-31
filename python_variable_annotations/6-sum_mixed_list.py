#!/usr/bin/env python3
"""list of floats annotations"""
from typing import List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """it returns the sum of mxd_lst"""
    return sum(mxd_lst)
