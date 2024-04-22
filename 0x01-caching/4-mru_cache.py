#!/usr/bin/env python3

"""
MRU Cache
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """Implements MRU Cache"""
    def __init__(self):
        """Calls parent constructor"""
        super().__init__()

    def put(self, key, item):
        """Updates Cache"""
        cached = self.cache_data
        if key is not None and item is not None:
            if len(cached) >= BaseCaching.MAX_ITEMS:
                r_key = list(cached.keys())[-1]
                print("DISCARD:", r_key)
                cached.pop(r_key)
            cached[key] = item

    def get(self, key):
        """Retreives an item from the cache"""
        cached = self.cache_data

        if key is None:
            return None
        data = cached.get(key, None)
        if data is not None:
            del cached[key]
            cached[key] = data
        return data
