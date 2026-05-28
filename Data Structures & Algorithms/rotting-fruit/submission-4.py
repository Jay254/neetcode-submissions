class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        #store all rotten fruits
        queue = deque([])
        fresh = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        
        minutes = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dx, dy in directions:
                    nx, ny = dx + r, dy + c
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx,ny))
            minutes += 1

        return minutes if fresh == 0 else -1