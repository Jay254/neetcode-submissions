class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # num_s = sum(ord(s[i]) for i in range(len(s)))
        # # num_t = sum(ord(t[i]) for i in range(len(t)))

        # # return num_s == num_t
        # arr_s = sorted([s[i] for i in range(len(s))])
        # arr_t = sorted([t[i] for i in range(len(t))])

        # return ''.join(arr_s) == ''.join(arr_t)
        return sorted(s) == sorted(t)