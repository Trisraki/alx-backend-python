#!/usr/bin/env python3
""" A function that sum_mixed_list which takes a list
mxd_lst of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sums list of of integers and floats """
    return sum(mxd_lst)
