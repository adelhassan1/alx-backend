#!/usr/bin/env python3
"""
BasicCache Module
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic dictionary
    """

    def __init__(self):
        """
        Initiliaze
        """
        self.cache_data = {}

    def put(self, key, item):
        """
        Adding value to the dict.
        """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Getting value from the dict.
        """
        if key not in self.cache_data or key is None:
            return None
        else:
            return self.cache_data[key]
