class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        INF = 2147483647
        directions = [(1,0), (-1,0), (0,-1), (0,1)]


        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j))

        while queue:
            i, j = queue.popleft()
            for dx, dy in directions:
                nx, ny = dx+i, dy+j
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == INF:
                    grid[nx][ny] = grid[i][j] + 1
                    queue.append((nx, ny))
