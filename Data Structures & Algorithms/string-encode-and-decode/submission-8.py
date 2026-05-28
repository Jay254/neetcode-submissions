class Solution:

    def encode(self, strs: List[str]) -> str:
        # if len(strs) == 0:
        #     return ''
        new = ''
        for i in strs:
            l = str(len(i)) + '#' + i
            new += l

        # new = ''.join(strs)
        return new

    def decode(self, s: str) -> List[str]:
        # if s == '':
        #     return []
        # elif s == ' ':
        #     return ['']
        # old = s.split()
        old = []
        i = 0
        while i < len(s):
            #get pref number
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1

            word = s[i: i+length]
            old.append(word)

            i += length

        return old