from math import isqrt
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1]*n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] > self.rank[ry]:
            self.par[ry] = rx
            self.rank[rx] += self.rank[ry]
        else:
            self.par[rx] = ry
            self.rank[ry] += self.rank[rx]
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if 1 in nums:   # 1 has no prime factors, can't connect
            return False

        uf = UnionFind(n)
        factor_map = {}

        for i, num in enumerate(nums):
            factors = self.factorize(num)
            for f in factors:
                if f in factor_map:
                    uf.union(i, factor_map[f])
                else:
                    factor_map[f] = i

        root0 = uf.find(0)
        for i in range(1, n):
            if uf.find(i) != root0:
                return False
        return True

    def factorize(self, x):
        factors = set()
        d = 2
        while d * d <= x:
            while x % d == 0:
                factors.add(d)
                x //= d
            d += 1
        if x > 1:
            factors.add(x)
        return factors
