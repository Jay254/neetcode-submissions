class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = j = 0

        while j < len(s):
            i = j
            while s[j] != '#':
                j += 1

            len_s = int(s[i:j])

            res.append(s[j+1:j+1+len_s])

            j += 1 + len_s

        return res
            
        