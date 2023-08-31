#!/usr/bin/env python3
"""list of floats annotations"""


def sum_list(input_list: list[float]) -> float:
    """it returns the sum of the float argument """

    res: float = 0

    for x in input_list:
        res += x
    
    return res
