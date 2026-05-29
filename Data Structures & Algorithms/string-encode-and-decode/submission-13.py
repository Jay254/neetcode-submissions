class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ''
        for s in strs:
            enc += str(len(s)) + '#' + s

        return enc

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            res.append(s[j+1:j+length+1])

            i = j + 1 + length

        return res

    