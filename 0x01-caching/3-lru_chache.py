#!/usr/bin/env python3
"""LRU caching mechanism"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Implementation of LRU"""
    def __init__(self):
        """Calls parent constructor"""
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
        """Retreives an item from the cache memory"""
        cached = self.cache_data

        if key is None:
            return None
        data = cached.get(key, None)
        if data is not None:
            """Move the accessed key to the end to
            represent it as the most recently use"""
            del cached[key]
            cached[key] = data
        return data
