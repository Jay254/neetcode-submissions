class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))

        heap = [(0, src, 0)] #cost, dest, stops
        best = {} #(city, stops) -> cost

        while heap:
            cost, city, stops = heapq.heappop(heap)
            if city == dst:
                return cost
            if stops > k:
                continue

            for nei, w in graph[city]:
                cur_cost = cost + w
                if (nei,stops+1) not in best or cur_cost < best[(nei, stops+1)]:
                    best[(nei, stops+1)] = cur_cost
                    heapq.heappush(heap, (cur_cost, nei, stops+1))

        return -1