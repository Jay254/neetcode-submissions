class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        
        # Initialize reachable matrices
        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        
        def dfs(r, c, reachable):
            reachable[r][c] = True
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < m and 0 <= new_c < n and not reachable[new_r][new_c] and heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r, new_c, reachable)
        
        # Start DFS from Pacific Ocean boundary (top row and left column)
        for i in range(m):
            dfs(i, 0, pacific_reachable)  # leftmost column (Pacific)
            dfs(i, n - 1, atlantic_reachable)  # rightmost column (Atlantic)
            
        for j in range(n):
            dfs(0, j, pacific_reachable)  # top row (Pacific)
            dfs(m - 1, j, atlantic_reachable)  # bottom row (Atlantic)
        
        # Collect cells that can reach both oceans
        result = []
        for r in range(m):
            for c in range(n):
                if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                    result.append([r, c])
        
        return result