class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        counter = Counter(tasks)
        heap = [-count for count in counter.values()]
        heapq.heapify(heap)
        queue = deque()

        while heap or queue:
            time += 1

            if heap:
                count = heapq.heappop(heap)
                count += 1
                if count != 0:
                    queue.append((count, time+n))
            if queue and queue[0][1] == time:
                count, _ = queue.popleft()
                heapq.heappush(heap, count)


            

        return time