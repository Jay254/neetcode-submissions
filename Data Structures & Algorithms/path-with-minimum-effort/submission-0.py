class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        m, n = len(heights), len(heights[0])
        heap = [(0, 0, 0)]
        distance = defaultdict()
        effort = [[float('inf')] * n for _ in range (m)]
        effort[0][0] = 0

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        while heap:
            cur_effort, r, c = heapq.heappop(heap)
            if r == m - 1 and c == n - 1:
                return cur_effort

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n:
                    diff = abs(heights[nr][nc] - heights[r][c])
                    new_effort = max(cur_effort, diff)
                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(heap,(new_effort, nr, nc))

            

