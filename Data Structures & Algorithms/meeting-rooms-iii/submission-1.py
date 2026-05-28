class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        num_meets = [0] * n
        meetings.sort()
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        busy_rooms = []

        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                end_time, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)

            duration = end - start
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                end_time, room = heapq.heappop(busy_rooms)
                heapq.heappush(busy_rooms, (end_time+duration, room))

            num_meets[room] += 1

        max_meets = max(num_meets)
        for i in range(n):
            if num_meets[i] == max_meets:
                return i


        

