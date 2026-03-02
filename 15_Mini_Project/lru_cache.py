"""
Project: LRU Cache Implementation
Description: Implements Least Recently Used (LRU) Cache
"""

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> value
        self.order = []  # track usage order

    def get(self, key):
        if key not in self.cache:
            print(f" Key {key} not found")
            return -1
        
        # Move key to end (most recently used)
        self.order.remove(key)
        self.order.append(key)
        
        print(f"Get {key} -> {self.cache[key]}")
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            # Update value and move to end
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used (first item)
            lru = self.order.pop(0)
            del self.cache[lru]
            print(f" Removed LRU key: {lru}")
        
        self.cache[key] = value
        self.order.append(key)
        print(f" Inserted {key} -> {value}")

    def display(self):
        print("\nCurrent Cache State:")
        for key in self.order:
            print(f"{key} -> {self.cache[key]}")


def main():
    print("=== LRU Cache Demo ===")
    cache = LRUCache(3)

    cache.put(1, "A")
    cache.put(2, "B")
    cache.put(3, "C")
    cache.display()

    cache.get(1)
    cache.put(4, "D")  # This should remove key 2
    cache.display()


if __name__ == "__main__":
    main()
