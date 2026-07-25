# Topic: Sets
# Phase: 3 - DSA
# Week: 1 - Day 3
# Description: Manual Set implementation using array of buckets (reusing HashMap logic)

class MySet:
    def __init__(self, size=10):
        # Initialize fixed-size array with empty lists (buckets)
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        # Convert key to an array index
        return hash(key) % self.size

    def add(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        # Do not add duplicate keys
        if key in bucket:
            return False

        bucket.append(key)
        return True

    def contains(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        # Return True if key exists in the bucket
        return key in bucket

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        # Delete key if found
        if key in bucket:
            bucket.remove(key)
            return True

        return False


def main():
    print("=== Creating MySet ===")
    my_set = MySet(size=5)

    print("\n--- Adding Elements ---")
    my_set.add(10)
    my_set.add(20)
    my_set.add(30)
    print("Added: 10, 20, 30")

    print("\n--- Duplicate Element Test ---")
    print("Adding 10 again...")
    added_again = my_set.add(10)
    print("Was 10 added again?", added_again)

    print("\n--- Contains Check ---")
    print("Contains 20?:", my_set.contains(20))
    print("Contains 50?:", my_set.contains(50))

    print("\n--- Removing Element ---")
    print("Removing 20...")
    my_set.remove(20)
    print("Contains 20 after removal?:", my_set.contains(20))


if __name__ == "__main__":
    main()