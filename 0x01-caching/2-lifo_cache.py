#!/usr/bin/env python3
"""Implements lifo cache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implements LIFO Cache"""
    def __init__(self):
        """Call parent constructor"""
        super().__init__()

    def put(self, key, item):
        """Updates cache"""

        cached = self.cache_data

        if key is not None and item is not None:
            if len(cached) >= BaseCaching.MAX_ITEMS:
                r_key = list(cached.keys())[-1]
                print("DISCARD:", r_key)
                cached.pop(r_key)
            cached[key] = item

    def get(self, key):
        """Retreives an item from the cache"""
        if key is None:
            return None
        data = self.cache_data.get(key, None)
        return data
