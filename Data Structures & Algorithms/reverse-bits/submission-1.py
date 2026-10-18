class Solution:
    def reverseBits(self, n: int) -> int:
        binary = format(n, '032b')
        return int(binary[::-1], 2)