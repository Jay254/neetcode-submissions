class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph  = defaultdict(list)
        for u,v,weight in times:
            graph[u].append((v,weight))

        heap = [(0,k)]

        shortest = {}

        while heap:
            time,node = heapq.heappop(heap)
            if node in shortest:
                continue
            
            shortest[node] = time
            for neighbor,weight in graph[node]:
                if neighbor not in shortest:
                    heapq.heappush(heap,(time+weight,neighbor))


        if len(shortest) == n:
            return max(shortest.values())
        else:
            return -1