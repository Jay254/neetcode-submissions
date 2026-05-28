class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        # a = {"act": ["act","cat"], "pots": ["pots","tops","stop"], "hat" : ["hat"]}
        for i,j in enumerate(strs):
            new = ''.join(sorted(j))
            if new in a:
                #k = a[new]
                a[new].append(j) # a = {"act":"act", "cat"}
            else:
                a[new] = [j] # a = {"act" : "act"}

        # ans = []
        # for i in a:
        #     ans.append(a[i])

        # return ans
        return list(a.values())


        