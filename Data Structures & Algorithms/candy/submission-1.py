class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n

        #left to right ensuring if num is bigger than it's left neighbor, it gets more candy
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
            
        #right to left ensuring if num is bigger than it's right neighbor it gets more
        for i in range(n-2, -1,-1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1]+1)

        return sum(candy)

        