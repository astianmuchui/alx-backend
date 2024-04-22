#!/usr/bin/python3

"""
This module demonstrates simple API pagination
"""


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:

    """Returns a tuple
    of the first page and the last page"""

    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a page of the dataset
        """
        assert page > 0 and isinstance(page, int)
        assert page_size > 0 and isinstance(page, int)
        start, end = index_range(page, page_size)

        if start >= len(self.dataset()) or end < 0:
            return []

        return self.dataset()[start:end]
