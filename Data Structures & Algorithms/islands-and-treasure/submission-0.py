class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        rows,cols = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            x,y = queue.popleft()

            for dx,dy in directions:
                nx,ny = x+dx, y+dy

                if 0 <= nx < rows and 0 <= ny <cols and grid[nx][ny] == INF:
                    grid[nx][ny] = grid[x][y] + 1
                    queue.append((nx,ny))
