#!/usr/bin/python3

"""
This module demonstrates simple API pagination
"""


def index_range(page, page_size):

    """Returns a tuple
    of the first page and the last page"""

    return (page - 1) * page_size, page * page_size
