class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def combinations(start, path):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start,n+1):
                path.append(i)
                combinations(i+1, path)
                path.pop()

        combinations(1, [])
        return res