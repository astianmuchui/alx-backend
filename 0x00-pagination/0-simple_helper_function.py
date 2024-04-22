#!/usr/bin/env python3

"""
This module demonstrates simple API pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:

    """Returns a tuple
    of the first page and the last page"""

    return ((page - 1) * page_size, page * page_size)
