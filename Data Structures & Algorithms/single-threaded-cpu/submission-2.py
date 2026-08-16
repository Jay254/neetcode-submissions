class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(e,p,i) for i, (e,p) in enumerate(tasks)])

        res = []
        heap = []
        i = 0
        time = 0
        while i < len(tasks) or heap:
            #cpu idle
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]

            while i < len(tasks) and tasks[i][0] <= time:
                e,p,idx = tasks[i]
                heapq.heappush(heap,(p,idx))
                i += 1
            
            #shortest available task
            p, idx = heapq.heappop(heap)
            time += p
            res.append(idx)

        return res