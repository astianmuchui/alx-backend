#!/usr/bin/env python3

"""
LFU Cache
"""
from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):

        """
        Initializes LFU Cache
        """
        super().__init__()
        self.frequency = defaultdict(int)

    def put(self, key, item):
        """
        Updates Cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            min_frequency = min(self.frequency.values())
            items_with_min_frequency = [k for k, v in self.frequency.items()
                                        if v == min_frequency]
            if len(items_with_min_frequency) > 1:
                lru_key = min(self.access_time,
                              key=lambda k: self.access_time[k])
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                print(f"DISCARD: {lru_key}")
            else:
                lfu_key = items_with_min_frequency[0]
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                print(f"DISCARD: {lfu_key}")

        self.cache_data[key] = item
        self.frequency[key] += 1
        self.access_time[key] = self.current_time
        self.current_time += 1

    def get(self, key):
        """Retreives from the cache"""
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.access_time[key] = self.current_time
        self.current_time += 1
        return self.cache_data[key]
