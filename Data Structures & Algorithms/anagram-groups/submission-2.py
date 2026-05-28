class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            sorted_s = tuple(sorted(s))
            dic[sorted_s].append(s)

        # print(dic)
        return list(dic.values())