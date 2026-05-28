class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #bfs
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        time = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dx, dy in directions:
                    nx, ny = dx+r, dy+c
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx,ny))
            time += 1

        return time if fresh == 0 else -1