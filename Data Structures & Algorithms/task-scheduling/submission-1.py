class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # #GREEDY
        # #freq of each task and retrieve max frequency
        # task_counts = Counter(tasks)
        # max_freq = max(task_counts.values())

        # #number of high freq tasks
        # max_freq_count = sum(1 for count in task_counts.values() if count == max_freq)

        # part_counts = max_freq - 1
        # part_length = n + 1
        # empty_slots = part_counts * part_length + max_freq_count

        # return max(len(tasks), empty_slots)

        #HEAP
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown = deque()

        while max_heap or cooldown:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap) + 1
                if count < 0:
                    cooldown.append((time+n, count))


            if cooldown and cooldown[0][0] == time:
                ready_time, ready_count = cooldown.popleft()
                heapq.heappush(max_heap, ready_count)

            
        return time