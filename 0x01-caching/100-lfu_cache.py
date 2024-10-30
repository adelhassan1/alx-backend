#!/usr/bin/env python3
"""
LFU Caching
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU Module
    """

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.usage_frequency = {}
        self.usage_order = []

    def put(self, key, item):
        """Add an item in the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.usage_frequency.values())
                lfu_keys = [
                        k
                        for k in self.usage_frequency
                        if self.usage_frequency[k] == min_freq
                ]

                if len(lfu_keys) > 1:
                    lfu_key = next(
                            k
                            for k in self.usage_order
                            if k in lfu_keys
                    )
                    self.usage_order.remove(lfu_key)
                else:
                    lfu_key = lfu_keys[0]
                    self.usage_order.remove(lfu_key)

                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self.usage_frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """Get an item by key."""
        if key is not None and key in self.cache_data:
            self.usage_frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
