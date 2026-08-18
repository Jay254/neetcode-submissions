class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        side = total // 4
        sides = [0] * 4
        
        matchsticks.sort(reverse=True)

        def backtrack(idx):
            if idx == len(matchsticks):
                return True

            stick = matchsticks[idx]
            for i in range(4):
                if sides[i] + stick <= side:
                    sides[i] += stick
                    if backtrack(idx+1):
                        return True

                    sides[i] -= stick
            return False

        return backtrack(0)

