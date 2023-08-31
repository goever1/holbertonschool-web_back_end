#!/usr/bin/env python3
"""Duck type and iteration"""
from typing import Iterable, Sequence, List, Union, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """it return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
