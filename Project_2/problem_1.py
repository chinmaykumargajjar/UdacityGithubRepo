import sys


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.count = dict()
        self.map = dict()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        ans = -1
        if key in self.map:
            if self.map[key]:
                ans = self.map[key]
                cnt = self.count[key] #Increment Count
                cnt += 1
                self.count[key] = cnt
        return ans

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        if len(self.count) >= self.capacity:
            #Iterate through map count and get least valued key
            #Remove it from self.map
            min_value = sys.maxsize
            temp_key = None
            for keyy,valuee in self.count.items():
                if valuee < min_value:
                    min_value = valuee
                    temp_key = keyy

            if temp_key:
                del self.map[temp_key]
                del self.count[temp_key]

        self.count[key] = 0 #initialize usage count to 0
        self.map[key] = value #set value to the key

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print(our_cache.get(None)) #Returns -1 because None doesn't exist

