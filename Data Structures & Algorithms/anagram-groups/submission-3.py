class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            
            ord_ch = [0] * 26
            for ch in s:
                ord_ch[ord(ch)-ord('a')] += 1

            dic[tuple(ord_ch)].append(s)

        return list(dic.values())
