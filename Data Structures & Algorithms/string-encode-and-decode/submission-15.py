class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        j = 0
        while j < len(s):
            length = 0
            while s[j] != '#':
                length = 10 * length + int(s[j])
                j += 1
            j += 1
            res.append(s[j:j+length])
            j = j + length

        return res