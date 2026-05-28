class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #freq of each task and retrieve max frequency
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())

        #number of high freq tasks
        max_freq_count = sum(1 for count in task_counts.values() if count == max_freq)

        part_counts = max_freq - 1
        part_length = n + 1
        empty_slots = part_counts * part_length + max_freq_count

        return max(len(tasks), empty_slots)