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
        """Updates cache"""

        cached = self.cache_data

        if key is not None and item is not None:
            if len(cached) >= BaseCaching.MAX_ITEMS:
                r_key = next(iter(cached))
                print("DISCARD:", r_key)
                cached.pop(r_key)
            cached[key] = item

    def get(self, key):
        """Retreives items from cache"""
        if key is None:
            return None
        result = self.cache_data.get(key, None)
        return result
