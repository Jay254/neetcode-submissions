class MyHashSet:

    def __init__(self):
        self.capacity = 1000
        self.buckets = [[] for i in range(self.capacity)]
    
    def _hash(self, key: int) -> int:
        return key % self.capacity

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if key not in self.buckets[idx]:
            self.buckets[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return key in self.buckets[idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)