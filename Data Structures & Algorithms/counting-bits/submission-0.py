class Solution:
    def countBits(self, n: int) -> List[int]:
        i = 0
        result = []
        while i <= n:
            count_ones = bin(i).count('1')
            print(count_ones)
            result.append(count_ones)
            i += 1

        return result