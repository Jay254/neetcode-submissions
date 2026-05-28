class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        atlantic = set()
        pacific = set()

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        #find atlantic ones, then pacific, then intersection

        def dfs(i, j, visited, prevHeight):
            if i < 0 or i >= m or j < 0  or j >= n:
                return

            if (i,j) in visited or heights[i][j] < prevHeight:
                return

            visited.add((i,j))
            for dx, dy in directions:
                dfs(i+dx, j+dy, visited, heights[i][j])
        
        # pacific
        for i in range(m): #rows
            dfs(i, 0, pacific, heights[i][0])
        for j in range(n): #cols
            dfs(0, j, pacific, heights[0][j])

        # atlantic
        for i in range(m):#rows
            dfs(i, n-1, atlantic, heights[i][n-1])
        for j in range(n):#cols
            dfs(m-1, j, atlantic, heights[m-1][j])

        res = list(pacific & atlantic)

        return res

