class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)] #elevation, r, c
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        while heap:
            time, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return time
            if visited[r][c]:
                continue
            visited[r][c] = True

            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    new_time = max(time, grid[nr][nc])
                    heapq.heappush(heap, (new_time, nr, nc))
