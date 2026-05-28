class MyHashMap:

    def __init__(self):
        self.capacity = 1000
        self.buckets = [[] for _ in range(self.capacity)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.capacity
        for i, (k,v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key,value)
                return
        self.buckets[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = key % self.capacity
        for k,v in self.buckets[idx]:
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        idx = key % self.capacity
        self.buckets[idx] = [(k,v) for (k,v) in self.buckets[idx] if k != key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)