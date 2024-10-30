#!/usr/bin/env python3
"""
LRU Caching
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU Module
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        Adding Items to the dict.
        """
        if key is None or item is None:
            return
        else:
            if key in self.cache_data:
                del self.cache_data[key]
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """
        Getting Items
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            item = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = item
            return self.cache_data[key]
