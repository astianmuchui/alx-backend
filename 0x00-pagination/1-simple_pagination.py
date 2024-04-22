#!/usr/bin/python3

"""
This module demonstrates simple API pagination
"""


import csv
import math
from typing import List


def index_range(page, page_size):

    """Returns a tuple
    of the first page and the last page"""

    return (page - 1) * page_size, page * page_size


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
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
