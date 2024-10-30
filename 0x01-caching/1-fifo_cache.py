#!/usr/bin/env python3
"""
FIFO Caching
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Caching
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        Adding items to dict.
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
            return self.cache_data[key]
