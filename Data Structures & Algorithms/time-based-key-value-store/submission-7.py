class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.dic[key])-1

        while l <= r:
            mid = (l+r) // 2
            val = self.dic[key][mid]

            if val[0] == timestamp:
                return val[1]
            elif val[0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1

        return self.dic[key][r][1] if r >= 0 else ""
