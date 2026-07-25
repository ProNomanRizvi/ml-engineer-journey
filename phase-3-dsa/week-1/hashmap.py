# Topic: HashMaps
# Phase: 3 - DSA
# Week: 1 - Day 2
# Description: Manual HashMap implementation using array of buckets (chaining)

class MyHashMap:
    def __init__(self, size=10):
        # Initialize fixed-size array with empty lists for chaining
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        # Convert key to an array index
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        # Update value if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Add new key-value pair if key does not exist
        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        # Search for key in bucket
        for k, v in bucket:
            if k == key:
                return v

        # Key not found
        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        # Delete key-value pair if found
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True

        return False


def main():
    print("=== Creating MyHashMap ===")
    my_map = MyHashMap(size=5)

    print("\n--- Inserting Keys ---")
    my_map.put("apple", 10)
    my_map.put("banana", 20)
    my_map.put("orange", 30)
    print("Inserted: 'apple' -> 10, 'banana' -> 20, 'orange' -> 30")

    print("\n--- Getting Values ---")
    print("Value for 'apple':", my_map.get("apple"))
    print("Value for 'banana':", my_map.get("banana"))
    print("Value for 'grape' (not found):", my_map.get("grape"))

    print("\n--- Updating Value ---")
    print("Updating 'apple' to 50...")
    my_map.put("apple", 50)
    print("New value for 'apple':", my_map.get("apple"))

    print("\n--- Removing Key ---")
    print("Removing 'banana'...")
    my_map.remove("banana")
    print("Value for 'banana' after removal:", my_map.get("banana"))


if __name__ == "__main__":
    main()