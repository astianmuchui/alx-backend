#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):

    """ FIFOCache implements a FIFO cache
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
