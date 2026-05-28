class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        n = len(s)
        a_to_b = {}
        b_to_a = {}

        for a, b in zip(s, t):
            if a in a_to_b and a_to_b[a] != b:
                return False
            if b in b_to_a and b_to_a[b] != a:
                return False
            
            a_to_b[a] = b
            b_to_a[b] = a

        return True