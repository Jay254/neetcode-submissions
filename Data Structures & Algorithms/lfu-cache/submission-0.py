class LFUCache:

    def __init__(self, capacity: int):
        #frequency -> keys have what freq
        #key, val, freq
        self.freq_keys = defaultdict(OrderedDict) # 1: (5,nOne),(7, none),(1,None)
        self.key_to_freq_vals = {} #key -> (val, freq)
        self.capacity = capacity
        self.min_freq = 0

    def _update(self, key):
        #get freq
        v, f = self.key_to_freq_vals[key]
        del self.freq_keys[f][key]
        if not self.freq_keys[f] and f == self.min_freq:
            self.min_freq += 1
        self.freq_keys[f+1][key] = None
        self.key_to_freq_vals[key] = (v, f+1)

    def get(self, key: int) -> int:
        if not key in self.key_to_freq_vals:#if not there
            return -1
        
        val, _ = self.key_to_freq_vals[key]
        #funtion to update freq
        self._update(key)
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        #update if present
        if key in self.key_to_freq_vals:
            self.key_to_freq_vals[key] = (value,self.key_to_freq_vals[key][1])
            self._update(key)

        #if capacity is reached
        if len(self.key_to_freq_vals) >= self.capacity:
            old_key, _ = self.freq_keys[self.min_freq].popitem(last=False)
            del self.key_to_freq_vals[old_key]

        #doesn't exist
        self.key_to_freq_vals[key] = (value, 1)
        self.freq_keys[1][key] = None
        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)