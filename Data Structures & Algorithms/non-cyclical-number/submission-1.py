class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        strn = str(n)
        char = list(strn)

        print(char)
        while True:
            tot = sum(int(ch) ** 2 for ch in char)
            if tot == 1:
                return True
            if tot in visited:
                return False
            else:
                char = str(tot)
                visited.add(tot)


        