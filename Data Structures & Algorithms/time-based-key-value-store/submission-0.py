class TimeMap:
    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.dic:
            self.dic[key] = []
            
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.dic:
            return ""

        pairs = self.dic[key]

        left, right = 0, len(pairs) - 1
        best_val = ""

        while left <= right:
            mid = (left+right) // 2

            if pairs[mid][0] <= timestamp:
                best_val = pairs[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return best_val
