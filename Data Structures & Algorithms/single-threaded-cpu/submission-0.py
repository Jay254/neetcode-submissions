class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        order = []

        time = 0
        i = 0
        n = len(tasks)
        tasks = sorted([(et,pt,i) for i, (et,pt) in enumerate(tasks)])

        while i < n or heap:
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]

            while i < n and tasks[i][0] <= time:
                et,pt,idx = tasks[i]
                heapq.heappush(heap, (pt,idx))
                i += 1

            pt, idx = heapq.heappop(heap)
            time += pt
            order.append(idx)

        return order