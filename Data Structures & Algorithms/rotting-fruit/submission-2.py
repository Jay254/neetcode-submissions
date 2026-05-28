class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        queue = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        

        minutes = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in directions:
                    nx, ny = dx+i, dy+j
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        queue.append((nx,ny))
                        fresh -= 1
                        grid[nx][ny] = 2

            minutes += 1

        return minutes if fresh == 0 else -1
