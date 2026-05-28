class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)
        heap = [-cnt for cnt in counts.values()]

        time = 0
        cooldown = []

        while heap or cooldown:
            time += 1

            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt != 0:
                    cooldown.append((time+n, cnt))

            if cooldown and cooldown[0][0] == time:
                _ , cnt = cooldown.pop(0)
                heapq.heappush(heap, cnt)


        return time
