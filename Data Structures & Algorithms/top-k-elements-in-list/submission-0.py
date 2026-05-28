class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        nums.sort()
        a = {}
        for i in nums:
            if i not in a:
                a[i] = 0
            a[i] += 1
        # {1: 1, 2: 2, 3: 3}

        sorted_dic = dict(sorted(a.items(), key = lambda item: item[1], reverse = True)[:k])

        arr = []

        return list(sorted_dic.keys())
        
        