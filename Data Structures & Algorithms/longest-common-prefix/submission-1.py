class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # pref = strs[0]
        # n = len(strs)

        # for i in range(1, n):
        #     j = min(len(pref), len(strs[i]))
        #     k = 0
        #     while k < j and pref[k] == strs[i][k]:
        #         k += 1
        #     pref = pref[:k]

        # return pref
        pref = strs[0]

        for s in strs[1:]:
            while not s.startswith(pref):
                pref = pref[:-1]

        return pref

