class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build graph
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # Priority Queue: (cost_so_far, current_city, stops_used)
        heap = [(0, src, 0)]

        # best[(city, stops)] = cost to reach
        best = dict()

        while heap:
            cost, city, stops = heapq.heappop(heap)

            # Found valid path
            if city == dst:
                return cost

            # If already seen this city with fewer stops, skip
            if (city, stops) in best and best[(city, stops)] <= cost:
                continue
            best[(city, stops)] = cost

            # Explore neighbors if within allowed stops
            if stops <= k:
                for neighbor, price in graph[city]:
                    heapq.heappush(heap, (cost + price, neighbor, stops + 1))

        return -1