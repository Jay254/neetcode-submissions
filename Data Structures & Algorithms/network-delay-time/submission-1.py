class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        dist = {i:float('inf') for i in range(1,n+1)}
        heap = [(0, k)]
        dist[k] = 0
        visited = set()

        while heap:
            cur_dist, u = heapq.heappop(heap)
            if u in visited:
                continue

            for v, w in graph[u]:
                new_dist = cur_dist + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

        max_t = max(dist.values())
        return max_t if max_t != float('inf') else -1
            
