#!/usr/bin/env python3
"""
MRU Caching
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRU Module
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        Adding items
        """
        if key is None or item is None:
            return
        else:
            if key in self.cache_data:
                del self.cache_data[key]
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data)[-2]
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        """
        Getting an item
        """
        if key is None or key not in self.cache_data:
            return None
        item = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = item
        return self.cache_data[key]
