class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # my solution
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

        #Gen AI solution
        # Step 1: Count frequencies of elements in the list
        frequency_map = Counter(nums)  # Counter({'1': 3, '2': 2, '3': 1})
    
        # Step 2: Use a heap to find the k most frequent elements
        return heapq.nlargest(k, frequency_map.keys(), key=frequency_map.get)

        
        