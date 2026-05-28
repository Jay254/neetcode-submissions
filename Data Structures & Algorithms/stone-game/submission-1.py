class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        #you can just return True since Alice will always win for an even-numbered pile
        dp = {}
        def dfs(l, r): #l,r being indices, and their length determines whose turn it is
            if l > r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]

            even = (r-l+1) % 2 #see if cur pile is even or odd
            #if even, it's Alices turn, if Odd its Bobb
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            dp[(l,r)] = max(dfs(l+1,r)+left, dfs(l,r-1)+right)

            return dp[(l,r)]

        total = sum(piles)
        alice_score = dfs(0, len(piles)-1)
        bobs_score = total - alice_score
        return alice_score > bobs_score

