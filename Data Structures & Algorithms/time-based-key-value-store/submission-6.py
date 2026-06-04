class TimeMap:

    def __init__(self):
        self.time_kv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_kv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.time_kv[key]
        l, r = 0, len(arr)-1
        res = ""
        while l <= r:
            mid = (l+r) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] <= timestamp:
                l = mid + 1
                res = arr[mid][1]
            else:
                r = mid - 1

        return res

