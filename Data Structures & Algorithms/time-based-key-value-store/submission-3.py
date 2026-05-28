class TimeMap:

    def __init__(self):
        self.arr = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.arr[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.arr or timestamp < self.arr[key][0][0]:
            return ""
        l, r = 0, len(self.arr[key])-1
        while l <= r:
            mid = (l+r) // 2
            t = self.arr[key][mid][0]
            if t < timestamp:
                l = mid + 1
            elif t > timestamp:
                r = mid - 1
            else:
                return self.arr[key][mid][1]

        return self.arr[key][r][1]