class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            res = [0] * 26
            for ch in s:
                res[ord(ch) - ord('a')] += 1
            
            dic[tuple(res)].append(s)

        return list(dic.values())