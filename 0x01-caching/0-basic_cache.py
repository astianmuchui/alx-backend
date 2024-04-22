#!/usr/bin/env python3
""" BaseCaching module
"""

from base import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache implements a simple cache
    """

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
