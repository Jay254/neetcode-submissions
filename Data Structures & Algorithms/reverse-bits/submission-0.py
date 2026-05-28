class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:][::-1]
        s = s.ljust(32, '0')
        reversed_int = int(s, 2)
        return reversed_int