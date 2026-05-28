class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)] 
        queue = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r,c))

        while queue:
            r,c = queue.popleft()
            for dx, dy in directions:
                nx, ny = dx+r, dy+c
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 2147483647:
                    grid[nx][ny] = min(grid[nx][ny], grid[r][c]+1)
                    queue.append((nx,ny))